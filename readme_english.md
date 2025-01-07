# NYC Yellow Data Scraper

Veja [readme Original](./readme.md)

## Objective
The **NYC Yellow Data Scraper** project aims to extract, filter, and organize data related to the trip records of yellow taxis available on the official NYC TLC (Taxi and Limousine Commission) website.  
This data is crucial for future analyses and service behavior predictions, contributing to understanding transportation patterns and improving urban planning. Furthermore, the project provides a structured foundation for predictive studies and data-driven decision-making initiatives.

---

## Prerequisites
To successfully run the project, ensure the following items are configured in your environment:

1. **Python 3.8+** installed and set up.
2. **Required Python libraries** listed in the `requirements.txt` file.
3. **Scrapy** properly installed.
4. A local folder configured to store the extracted data.

---

## Basic Commands
Run the following commands in the terminal to execute the project:

1. Install the project dependencies:  
   ```
   pip install -r requirements.txt
   ```

2. Navigate to the Scrapy project directory:  
   ```
   cd yellow_tlc
   ```

3. Run the crawler with the following command:  
   ```
   scrapy crawl yellow_tripdata
   ```

To configure specific dates or change the download folder, customize the variables in the `settings.py` file or pass arguments when running the crawler.

---

## Directory Structure
Below is the structure of the Scrapy project:

```
yellow_tlc/
├── landing/                # Directory to store the extracted files
├── spiders/                # Directory containing the spider files
│   └── yellow_tripdata.py  # Main spider for data extraction
├── settings.py             # Scrapy settings
├── requirements.txt        # Required libraries
└── ...
```

---

## Request Control
The following code snippet in the `settings.py` file was implemented to manage crawler requests:

```python
# Configuration to avoid server overload
DOWNLOAD_DELAY = 2  # Sets a 2-second delay between requests
AUTOTHROTTLE_ENABLED = True  # Enables automatic request throttling
AUTOTHROTTLE_START_DELAY = 1  # Initial delay for autothrottle
AUTOTHROTTLE_MAX_DELAY = 10  # Maximum delay between requests
```

### Impact
This configuration reduces the frequency of consecutive requests, helping to prevent blocks and ensuring the target server is respected.

---

## Conclusion and Flexibility
The **NYC Yellow Data Scraper** project offers a robust and configurable approach to extracting yellow taxi data from New York City. The crawler was designed to allow customization of critical variables, such as `start_urls`, `start_date`, `end_date`, and `landing_dir` directly in the crawler.  

Additionally, the project can be easily integrated into automation pipelines, such as those orchestrated by **Apache Airflow**, making it a powerful and flexible tool for large-scale applications.
