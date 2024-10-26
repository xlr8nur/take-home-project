from itemadapter import ItemAdapter

from infra.postgresql_connector import PostgreSQLConnector
from infra.redis_connector import RedisConnector
import json
import os
from dotenv import load_dotenv

load_dotenv()

class JobsProjectPipeline:
    def __init__(self):
           self.db = PostgreSQLConnector(
               host=os.getenv('POSTGRES_HOST'),
               database=os.getenv('POSTGRES_DB'),
               user=os.getenv('POSTGRES_USER'),
               password=os.getenv('POSTGRES_PASSWORD')
           )
           self.db.create_table()
           self.redis = RedisConnector(
               host=os.getenv('REDIS_HOST'),
               port=int(os.getenv('REDIS_PORT')),
               db=int(os.getenv('REDIS_DB'))
           )

    def process_item(self, item, spider):
        item_id = item.get('slug')

        if self.redis.is_item_cached(item_id):
            print(f"Item {item_id} is already cached, moving on.")
            return item

        print(f"Item with slug {item_id} added to Redis and DB.")
        self.redis.cache_item(item_id, json.dumps(dict(item)))
        self.db.insert_job(item)
        return item

    def close_spider(self, spider):
        self.db.close()
        self.redis.close()
