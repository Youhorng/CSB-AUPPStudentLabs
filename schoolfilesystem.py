
#Libraries you may need:
import csv
import collections
import os
import pandas as pd 
import urllib.request
from bs4 import BeautifulSoup


#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        self.data = None


    def process_file(self, file_path):           
        
        try:
            with open(file_path, 'r') as file:
                if file_path.endswith('.csv'):
                    self.data = pd.read_csv(file_path)
                elif file_path.endswith('.txt'):
                    self.data = file.read()
                else:
                    self.data = None
            if file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)
            
            return self.data
        
        except FileNotFoundError:
            print('File not found')


    def transfer_data(self, old_file_path, new_file_path):

        try:
            with open(new_file_path, 'a') as file:
                file.write(str(self.process_file(old_file_path)))
        except UnicodeDecodeError:
            print('File not found')


    def fetch_web_data(self, url):
        
        # Open the URL and read the HTML content
        response = urllib.request.urlopen(url)
        html_content = response.read()

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        return soup.get_text()


    def analyze_content(self):

        grade10_df = self.process_file('student_grade_10.csv')
        total_grade10_average = grade10_df['Average'].mean()
        subject_averages_10 = grade10_df[['Math', 'Chemistry', 'Physics', 'Biology', 'History']].mean()
        class_subject_averages_10 = grade10_df.groupby('Class')[['Math', 'Chemistry', 'Physics', 'Biology', 'History']].mean()
        highest_average_each_class_10 = class_subject_averages_10.idxmax(axis=1)
        grade_10_data = [total_grade10_average, subject_averages_10, class_subject_averages_10, highest_average_each_class_10]

        grade11_df = self.process_file('student_grade_11.csv')
        total_grade11_average = grade11_df['Average'].mean()
        subject_averages_11 = grade11_df[['Math', 'Chemistry', 'Physics', 'Biology', 'History']].mean()
        class_subject_averages_11 = grade11_df.groupby('Class')[['Math', 'Chemistry', 'Physics', 'Biology', 'History']].mean()
        highest_average_each_class_11 = class_subject_averages_11.idxmax(axis=1)
        grade_11_data = [total_grade11_average, subject_averages_11, class_subject_averages_11, highest_average_each_class_11]

        grade12_df = self.process_file('student_grade_12.csv')
        total_grade12_average = grade12_df['Average'].mean()
        subject_averages_12 = grade12_df[['Math', 'Chemistry', 'Physics', 'Biology', 'History']].mean()
        class_subject_averages_12 = grade12_df.groupby('Class')[['Math', 'Chemistry', 'Physics', 'Biology', 'History']].mean()
        highest_average_each_class_12 = class_subject_averages_12.idxmax(axis=1)
        grade_12_data = [total_grade12_average, subject_averages_12, class_subject_averages_12, highest_average_each_class_12]

        return grade_10_data, grade_11_data, grade_12_data


    def generate_summary(self):
        
        # Average report
        grade_10_data, grade_11_data, grade_12_data = self.analyze_content()

        print('1. Overall School Average')
        print(' Grade 10: ', round(grade_10_data[0], 2))
        print(' Grade 11: ', round(grade_11_data[0], 2))
        print(' Grade 12: ', round(grade_12_data[0], 2))
        print(' Total School Average', round((grade_10_data[0] + grade_11_data[0] + grade_12_data[0])/3, 2))
        
        print()

        print('2. Average by Subject')
        print('=================================================')
        print('   Grade 10 Subject Average')
        print('        Math      :', grade_10_data[1]['Math'])
        print('        Chemistry :', grade_10_data[1]['Chemistry'])
        print('        Physics   :', grade_10_data[1]['Physics'])
        print('        Biology   :', grade_10_data[1]['Biology'])
        print('        History   :', grade_10_data[1]['History'])
        print('=================================================')
        print('   Grade 11 Subject Average')
        print('        Math      :', grade_11_data[1]['Math'])
        print('        Chemistry :', grade_11_data[1]['Chemistry'])
        print('        Physics   :', grade_11_data[1]['Physics'])
        print('        Biology    :', grade_11_data[1]['Biology'])
        print('        History   :', grade_11_data[1]['History'])
        print('=================================================')
        print('   Grade 12 Subject Average')
        print('        Math      :', grade_12_data[1]['Math'])
        print('        Chemistry :', grade_12_data[1]['Chemistry'])
        print('        Physics   :', grade_12_data[1]['Physics'])
        print('        Biology    :', grade_12_data[1]['Biology'])
        print('        History   :', grade_12_data[1]['History'])

        print()

        print('3. Average Subject By classes')
        print('=============================================================')
        print('    Grade 10 Class Average Subject')
        print(grade_10_data[2])
        print('=============================================================')
        print('    Grade 11 Class Average Subject')
        print(grade_11_data[2])
        print('=============================================================')
        print('    Grade 12 Class Average Subject')
        print(grade_12_data[2])

        print()

        print('4. Highest Grade Report in each class')
        print('=================================================')
        print('    Grade 10')
        print('         Class A ', grade_10_data[3]['A'])
        print('         Class B ', grade_10_data[3]['B'])
        print('         Class C ', grade_10_data[3]['C'])
        print('=================================================')
        print('    Grade 11')
        print('         Class A ', grade_11_data[3]['A'])
        print('         Class B ', grade_11_data[3]['B'])
        print('         Class C ', grade_11_data[3]['C'])
        print('=================================================')
        print('    Grade 12')
        print('         Class A ', grade_12_data[3]['A'])
        print('         Class B ', grade_12_data[3]['B'])
        print('         Class C ', grade_12_data[3]['C'])


sss = SchoolAssessmentSystem()

sss.generate_summary()

