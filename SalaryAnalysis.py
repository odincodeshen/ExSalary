# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:09:37 2015

@author: shenlunming

@package:
    1. pyinstaller --onefile MyScript.py
    2. exe file will locate on dist floder
    2. http://joelee-testing.blogspot.tw/2015/01/pyinstaller-python-script.html

"""

'''
""" Add %matplotlib inline once we want run on iPython """
%matplotlib inline
'''

import csv
import sys
import matplotlib.pyplot as plt
from decimal import *

if (sys.version_info.major != 2):
    print('This py file only executed on python2')
    raise AssertionError

logfile = 'SalaryLog.txt'
record_list = []
NtdSalaryList = []
PreLog = []
PreClass = []

'''
Cny2Usd_conv_Usd2Ntd = []
'''

'''
def dailyRecord(SalaryDate, UsdSalary, NtdSalary, Cny2UsdRate, Usd2NtdRate):
    return {
        'SalaryDate': SalaryDate,
        'UsdSalary': UsdSalary,
        'NtdSalary': NtdSalary,
        'Cny2UsdRate': Cny2UsdRate,
        'Usd2NtdRate': Usd2NtdRate,
        'Cny2NtdRate': Cny2NtdRate
    }
'''


## record class for daily report
class dailyRecord:
    def __init__(self, SalaryDate, UsdSalary, NtdSalary, Cny2UsdRate, Usd2NtdRate, Cny2NtdRate):
        self.SalaryDate  = SalaryDate
        self.UsdSalary   = UsdSalary
        self.NtdSalary   = NtdSalary
        self.Cny2UsdRate = Cny2UsdRate
        self.Usd2NtdRate = Usd2NtdRate
        self.Cny2NtdRate = Cny2NtdRate

    def __str__(self):
        string = str(self.SalaryDate) + ',\t' + str(self.UsdSalary) + ',\t' + str(self.NtdSalary)
        return string


## Load log from CSV file which produced by CalSalaryExRate.py ##
with open(logfile, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    analysis_list = list(spamreader)


## Pass the first line ##
analysis_list = analysis_list[1:]
'''
print analysis_list
'''

## Sort all log by date ##
analysis_list = sorted(analysis_list, key=lambda x: x[0])


## Create record class and link ##
for item in analysis_list:
    '''
    usd2ntd_conv_cny2usd = float(Decimal(item[4][1:])) * float(Decimal(item[5][1:]))
    Cny2Usd_conv_Usd2Ntd.append(usd2ntd_conv_cny2usd)
    '''

    ## Remove duplicate daily log by DATE ##
    if ( item[0] == PreLog ):
        record_list.pop()

    ## Create class for ecah of log ##
    record_list.append(
                    dailyRecord(
                        item[0],
                        float(Decimal(item[2][1:])),
                        float(Decimal(item[3][1:])),
                        float(Decimal(item[4][1:])),
                        float(Decimal(item[5][1:])),
                        float(Decimal(item[6][1:]))
                    )
                )
    PreLog = item[0]
'''    PreClass = newRecord   '''


## Traverse all class on the record_list ##
print '\n\nList all record'
for class_num in range(len(record_list)):
    record_list[class_num].NtdSalary
    record_list[class_num].SalaryDate
    NtdSalaryList.append(record_list[class_num].NtdSalary)
    print(record_list[class_num].NtdSalary)


plt.plot(NtdSalaryList)


print '\n\nToday\'s record'
print record_list[len(record_list)-1]
