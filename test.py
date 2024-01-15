import csv
import collections
import os
import pandas as pd 
import urllib.request
from bs4 import BeautifulSoup

class SchoolAssessmentSystem:
    def __init__(self):
        self.data = None

    def process_file(self, file_path):            
        try: 
            with open(file_path, 'r') as file:
                self.data = file.read()
            return self.data
        except FileNotFoundError:
            print('File not found')
            return None

    def transfer_data(self, old_file_path, new_file_path):

        try:
            with open(new_file_path, 'a') as file:
                file.write(self.process_file(old_file_path))
        except UnicodeDecodeError:
            print('File not found')


    def fetch_web_data(self, url):
        
        # Open the URL and read the HTML content
        response = urllib.request.urlopen(url)
        html_content = response.read()

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        return soup.get_text()

    def analyze_content():
        pass

    def generate_summary():
        pass


sss = SchoolAssessmentSystem()
# sss.transfer_data('file2.csv', 'new_file1.csv')

print(sss.fetch_web_data('https://nces.ed.gov/'))
