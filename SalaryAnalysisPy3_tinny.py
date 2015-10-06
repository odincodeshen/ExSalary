# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:09:37 2015

@author: shenlunming

@package:
    1. pyinstaller --onefile MyScript.py
    2. exe file will locate on dist floder
    2. http://joelee-testing.blogspot.tw/2015/01/pyinstaller-python-script.html

"""

import sys
import csv

'''from decimal import *'''

'''
""" Add %matplotlib inline once we want run on iPython """
%matplotlib inline
'''

if (sys.version_info.major != 3):
    print('This py file only executed on python3')
    raise AssertionError

logfile = 'SalaryLog.txt'
record_list = []
NtdSalaryList = []
PreLog = []
PreClass = []


# record class for daily report #
class dailyRecord:
    def __init__(self, SalaryDate, UsdSalary, NtdSalary,
                 Cny2UsdRate, Usd2NtdRate, Cny2NtdRate):
        self.SalaryDate = SalaryDate
        self.UsdSalary = UsdSalary
        self.NtdSalary = NtdSalary
        self.Cny2UsdRate = Cny2UsdRate
        self.Usd2NtdRate = Usd2NtdRate
        self.Cny2NtdRate = Cny2NtdRate

    def __str__(self):
        string = str(self.SalaryDate) + ',\t'
        string += str(self.UsdSalary) + ',\t' + str(self.NtdSalary)
        return string


# Load log from CSV file which produced by CalSalaryExRate.py #
with open(logfile, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    analysis_list = list(spamreader)

# Pass the first line #
analysis_list = analysis_list[1:]
print('Total log count:   %s' % len(analysis_list))

# Sort all log by date #
analysis_list = sorted(analysis_list, key=lambda x: x[0])

# Create record class and link #
for item in analysis_list:
    # Remove duplicate daily log by DATE #
    if (item[0] == PreLog):
        record_list.pop()

    # Create class for ecah of log #
    record_list.append(
                    dailyRecord(
                        item[0],
                        float(float(item[2][1:])),
                        float(float(item[3][1:])),
                        float(float(item[4][1:])),
                        float(float(item[5][1:])),
                        float(float(item[6][1:]))
                    )
                )
    PreLog = item[0]

print('Total daily count: %s' % len(record_list))

# Traverse all class on the record_list #
print('\n\nList all record')
for class_num in range(len(record_list)):
    record_list[class_num].NtdSalary
    record_list[class_num].SalaryDate
    NtdSalaryList.append(record_list[class_num].NtdSalary)
    print(record_list[class_num].NtdSalary)

print('\n\nToday\'s record')
print(record_list[len(record_list)-1])
'''

dailyRecordObj = dailyRecord(
                     str(20151006),
                     float(23000),
                     float(3714.5),
                     float(0.1615),
                     float(30.86),
                     float(4.95700)
                )
record_list.append(dailyRecordObj)

print(record_list[0])
print(record_list[0].Cny2NtdRate)
'''
