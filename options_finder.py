# This class will take a look at the file beginner_python_code.csv and it will print the days and topics as a menu.

import csv
import os
import time


class Finder:
    """Assigns self.day and self.option as string"""

    def __init__(self):
        self.day = 0
        self.option = 0
        self.days = []
        self.options = []

    def select_day(self):
        """ Search the file beginner_python_code.csv and ask for a string value for the day"""
        x = 0
        self.days = []
        with open('./beginner_data/beginner_python_code.csv', 'r') as file:
            read_csv = csv.reader(file)
            for row in read_csv:
                if row[0] != '' and row[0] != 'Days':
                    if row[0] not in self.days:
                        self.days.append(row[0])
                        x += 1
                        print(f'{x}. {row[0]}')
            try:
                self.day = int(input('Please type the number of the date that you want to check: '))
                if self.day < 1 or self.day > len(self.days):
                    print('Ops.. Select one number from the list')
                    time.sleep(1)
                    print("\n" * 10)
                    self.select_day()
                else:
                    print("\n" * 10)
                    self.select_option(self.day, self.days)
            except ValueError:
                print('Ops.. Bad Value please insert a valid input')
                time.sleep(1)
                print("\n" * 10)
                self.select_day()

    def select_option(self, day, days):
        """ Search the file beginner_python_code.csv and ask for a string value for the option day"""
        x = 0
        with open('./beginner_data/beginner_python_code.csv', 'r') as file:
            read_csv = csv.reader(file)
            for row in read_csv:
                if row[0] == days[day - 1] and row[1] != 'Lesson':
                    x += 1
                    self.options.append(row[1])
                    print(f'{x}. {row[1]}: {row[2]}')
            try:
                self.option = int(input('\nPlease type the number of the option that you want to check: '))
                if self.option < 1 or self.option > len(self.options):
                    print('Ops.. Select one number from the list')
                    self.select_day()
                else:
                    time.sleep(2)
                    print("\n" * 15)
            except ValueError:
                print('Ops.. Bad Value please insert a valid input')
                self.select_day()
