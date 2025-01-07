import os
import re
from datetime import datetime

import scrapy


class YellowTripDataSpider(scrapy.Spider):
    name = "yellow_tripdata"

    # Variables to be configured dynamically
    custom_settings = {
        # Default URL
        'start_urls': ['https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'],
        'start_date': '2024-07',  # Default start date
        'end_date': '2024-12',    # Default end date
        'landing_dir': 'landing',  # Default directory to save files
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize configurable variables
        self.start_urls = kwargs.get(
            'start_urls', self.custom_settings['start_urls'])
        self.start_date = kwargs.get(
            'start_date', self.custom_settings['start_date'])
        self.end_date = kwargs.get(
            'end_date', self.custom_settings['end_date'])
        self.landing_dir = kwargs.get(
            'landing_dir', self.custom_settings['landing_dir'])

    def parse(self, response):
        # Select all <a> tags with href containing "yellow_tripdata"
        links = response.css('a[href*="yellow_tripdata"]::attr(href)').getall()

        # Ensure the landing directory exists
        if not os.path.exists(self.landing_dir):
            os.makedirs(self.landing_dir)

        # Filter links based on the date range
        for link in links:
            # Ensure the link is absolute
            if not link.startswith('http'):
                link = response.urljoin(link)

            # Extract the date from the link using regex
            date_match = re.search(r'\d{4}-\d{2}', link)
            if date_match:
                date_str = date_match.group()
                # Check if the date is within the defined range
                if self.is_date_in_range(date_str):
                    # Make a new request for the link and call the parse_file method
                    yield scrapy.Request(url=link, callback=self.parse_file)

    def is_date_in_range(self, date_str):
        """Checks if the date in yyyy-mm format is within the defined range."""
        try:
            date = datetime.strptime(date_str, "%Y-%m")
            start = datetime.strptime(self.start_date, "%Y-%m")
            end = datetime.strptime(self.end_date, "%Y-%m")
            return start <= date <= end
        except ValueError:
            return False

    def parse_file(self, response):
        # Extract the file name from the link
        file_name = response.url.split('/')[-1]
        file_path = os.path.join(self.landing_dir, file_name)

        # Save the file content to disk
        with open(file_path, 'wb') as f:
            f.write(response.body)

        self.log(f"File saved: {file_path}")
