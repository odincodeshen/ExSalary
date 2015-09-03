# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:09:37 2015

@author: shenlunming

@package: 
    1. pyinstaller --onefile MyScript.py
    2. exe file will locate on dist floder
    2. http://joelee-testing.blogspot.tw/2015/01/pyinstaller-python-script.html

"""

from decimal import *
import csv
import matplotlib.pyplot as plt


logfile = 'SalaryLog.txt'
'''
logfile = 'SalaryLogTemp3.txt'
'''

SalaryDate = []
UsdSalary = []
NtdSalary = []

Cny2UsdRate = []
Usd2NtdRate = []
Cny2NtdRate = []

record_list = []

Cny2Usd_conv_Usd2Ntd = []

def dailyRecord(SalaryDate, UsdSalary, NtdSalary, Cny2UsdRate, Usd2NtdRate):
    return {
        'SalaryDate': SalaryDate,
        'UsdSalary': UsdSalary,
        'NtdSalary': NtdSalary,
        'Cny2UsdRate': Cny2UsdRate,
        'Usd2NtdRate': Usd2NtdRate,
        'Cny2NtdRate': Cny2NtdRate
    }

with open(logfile, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    analysis_list = list(spamreader)

print analysis_list
''' pass the first line '''
analysis_list = analysis_list[1:]
print analysis_list

for item in analysis_list:
    SalaryDate.append(item[0])
    UsdSalary.append(float(Decimal(item[2][1:])))
    NtdSalary.append(float(Decimal(item[3][1:])))
    Cny2UsdRate.append(float(Decimal(item[4][1:])))
    Usd2NtdRate.append(float(Decimal(item[5][1:])))
    Cny2NtdRate.append(float(Decimal(item[6][1:])))
    usd2ntd_conv_cny2usd = float(Decimal(item[4][1:])) * float(Decimal(item[5][1:]))
    Cny2Usd_conv_Usd2Ntd.append(usd2ntd_conv_cny2usd)
    newRecord = dailyRecord(
        item[0],
        float(Decimal(item[2][1:])),
        float(Decimal(item[3][1:])),
        float(Decimal(item[4][1:])),
        float(Decimal(item[5][1:]))
    )
    record_list.append(newRecord)

'''
print SalaryDate
print UsdSalary
print NtdSalary
print Cny2UsdRate
print Usd2NtdRate
'''

for date in record_list:
    date = date['SalaryDate']
    print date

for money in record_list:
    money = money['UsdSalary']
    print money

print Usd2NtdRate
print Cny2UsdRate
'''
USD2NTD_div_CNY2USD = Usd2NtdRate / Cny2UsdRate
'''
print Cny2Usd_conv_Usd2Ntd

'''plt.plot(UsdSalary)'''
plt.plot(NtdSalary)

print '\n\nToday\'s record'
print record_list[len(record_list)-1]
print 'End Python\n\n'

