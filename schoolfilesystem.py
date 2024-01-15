
#Libraries you may need:
import csv
import collections
import os
import pandas as pd 
import requests 
from bs4 import BeautifulSoup

#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        self.data = None


    def process_file(self, file_path):           
        
        try:
            with open(file_path, 'r') as file:
                if file_path.endswith('.csv'):
                    self.data = list(csv.reader(file))
                elif file_path.endswith('.txt'):
                    self.data = file.read()
                else:
                    self.data = None
            if file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)

        except FileNotFoundError:
            print('File not found')


    def transfer_data():
        pass


    def fetch_web_data(self, url):
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx status codes)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            return soup.get_text()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None


    def analyze_content():
        pass


    def generate_summary():
        pass


sss = SchoolAssessmentSystem()
# sss.process_file('data.csv')
# print(sss.data)

print(sss.fetch_web_data('https://www.google.com/'))

