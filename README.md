# Take-Home-Project

This project is to develop a scraping pipeline using Python and Scrapy, which extracts data from a JSON file, stores it in PostgreSQL database, and uses Redis for caching. The entire application containerized using Docker and orchestrated with Docker Compose.


## Requirements

- Docker and Docker Compose

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/xlr8nur/take-home-project.git
   cd take-home-project
   ```

2. **Install Dependencies**:
   Ensure Docker and Docker Compose are installed on your system.

3. **Start Services**:
   Run the following command to build and start services:
   ```bash
   docker-compose up --build
   ```

## Scrapy Project Setup

This project uses Scrapy to extract data from JSON files located locally. The data is stored in PostgreSQL, and Redis is used to cache data to avoid duplicate processing.

- `json_spider.py` spider reads JSON data and sends it through pipelines.
- `DatabasePipeline` handles saving data to PostgreSQL.
- `CachePipeline` caches data in Redis.

## Running the Scraper

Once the Docker containers are up, you can run the spider within the container:
   ```bash
   docker-compose run scrapy crawl job_spider
   ```

## Export Data to CSV

To export the stored data from PostgreSQL to a CSV file:
   ```bash
   docker-compose run scrapy python query.py
   ```

## Notes

- Ensure that any raw JSON files are correctly referenced in `json_spider.py`.
- Make sure to document any additional changes or configurations in this file as needed.
