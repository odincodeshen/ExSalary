# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:54:12 2015

@author: shenlunming

@description: auto calculation the exchange rate from my salary

@package:
    1. pyinstaller --onefile CalSalaryExRate.py
    2. exe file will locate on dist floder
    2. http://joelee-testing.blogspot.tw/2015/01/pyinstaller-python-script.html
"""

# import httplib
import requests
from string import split
import datetime
import os.path
import shutil


Salary_CNY = 23000


X_2_NTD_RATE_URL = "rate.bot.com.tw"
X_2_NTD_RATE_PAGE = "/Pages/Static/UIP003.zh-TW.htm"

CNY_2_USD_RATE_URL = "www.findrate.tw"
CNY_2_USD_RATE_PAGE = "/converter/CNY/USD/100/"

SEARCH_USD_2_NTD = "美金 (USD)"
SEARCH_CNY_2_NTD = "人民幣 (CNY)"
SEARCH_CNY_2_USD = "1 CNY = "


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)


'''
Get Current Exchange Rate
USD -> NTD : rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm
CNY -> NTD : rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm
'''


'''
"2015/08/25"
ExchangeRate_USD2NTD = 32.57000
ExchangeRate_CNY2NTD = 5.00200
ExchangeRate_CNY2USD = 0.1552
'''
"2015/08/25"
ExchangeRate_USD2NTD = 32.57000
ExchangeRate_CNY2NTD = 5.00200
ExchangeRate_CNY2USD = 0.1552


today = datetime.date.today()
print(today)

exchangeURL = X_2_NTD_RATE_URL
exchangePage = X_2_NTD_RATE_PAGE
currency = SEARCH_USD_2_NTD
'''
exchangeURL =  "rate.bot.com.tw"
exchangePage = "/Pages/Static/UIP003.zh-TW.htm"
'''

''' Get USD->NTD '''
# Python 2
# conn = httplib.HTTPConnection(exchangeURL, 80)
# conn.request("GET", exchangePage)
# reader = conn.getresponse()
# pageContext = reader.read()

res = requests.get(url)
res.raise_for_status()

# Python 2
# print "Fetch \"美金 (CNY)\" CNY->NTD from " + exchangeURL + exchangePage
# Python 3
string = 'Fetch \"美金 (USD)\" USD->NTD from '
string += str(exchangeURL) + str(exchangePage)
print(string)

indess = pageContext.find(currency)
pageContext = pageContext[indess:(indess+500)]
exchange = split(split(pageContext, ">")[6], "<")[0]
# Python 2
# print "    --> " + exchange
# Python 3
print('    --> ' + str(exchange))
ExchangeRate_USD2NTD = float(exchange)
conn.close()


''' Get CNY->NTD '''
currency = SEARCH_CNY_2_NTD
conn = httplib.HTTPConnection(exchangeURL, 80)
conn.request("GET", exchangePage)
reader = conn.getresponse()
pageContext = reader.read()

# Python 2
# print "Fetch \"人民幣 (CNY)\" CNY->NTD from " + exchangeURL + exchangePage
# Python 3
string = 'Fetch \"人民幣 (CNY)\" CNY->NTD from '
string += str(exchangeURL) + str(exchangePage)
print(string)

indess = pageContext.find(currency)
pageContext = pageContext[indess:(indess+500)]
exchange = split(split(pageContext, ">")[6], "<")[0]
# Python 2
# print "    --> " + exchange
# Python 3
print('    --> ' + str(exchange))
ExchangeRate_CNY2NTD = float(exchange)
conn.close()


''' Get USD->CNY '''
'''
exchangeURL =  "www.findrate.tw"
exchangePage = "/converter/CNY/USD/100/"
'''
exchangeURL = CNY_2_USD_RATE_URL
exchangePage = CNY_2_USD_RATE_PAGE
currency = SEARCH_CNY_2_USD

# Python 2
# print "Fetch \"1 CNY\" USB->CNY from " + exchangeURL + exchangePage
# Python 3
string = 'Fetch \"1 CNY\" USB->CNY from '
string += str(exchangeURL) + str(exchangePage)
print(string)

conn = httplib.HTTPConnection(exchangeURL, 80)
conn.request("GET", exchangePage)
reader = conn.getresponse()
pageContext = reader.read()

indess = pageContext.find(currency)
pageContext = pageContext[indess+8:(indess+15)]
exchange = split(pageContext, " ")[0]
# Python 2
# print "    --> " + exchange
# Python 3
print('    --> ' + str(exchange))
ExchangeRate_CNY2USD = float(exchange)
conn.close()

'''
print "--USD->NTD--"
print ExchangeRate_USD2NTD
print "--CNY->NTD--"
print ExchangeRate_CNY2NTD
print "--CNY->USD--"
print ExchangeRate_CNY2USD
print "------------"
'''

"2015/07/01"
'''
ExchangeRate_USD2NTD = 30.86000
ExchangeRate_CNY2NTD = 4.95700
ExchangeRate_CNY2USD = 0.1615
'''

Salary_CNY2USD = Salary_CNY * ExchangeRate_CNY2USD
Salary_USD2NTD = Salary_CNY2USD * ExchangeRate_USD2NTD

print('......')
print('Got USD' + str(Salary_CNY2USD))
print('Got NTD' + str(Salary_USD2NTD))
print('......')

''' Log the Salary_CNY2USD / Salary_USD2NTD into file '''
''' DATE,	CNY_SALARY,	TO_USD,	TO_NTD,	CNY2USD,	USD2NTD,	CNY2NTD '''

if os.path.isfile('SalaryLog.txt'):
    log_f = open('SalaryLog.txt', 'a+')
else:
    log_f = open('SalaryLog.txt', 'a+')
    string = 'DATE,	CNY_SALARY,	TO_USD,	TO_NTD,	CNY2USD,	USD2NTD,	CNY2NTD\n'
    log_f.write(string)
    string = '2015-07-01,\t23000,\t3714.5,\t114629.47,'
    string += '\t0.1615,\t30.86000,\t4.95700\n'
    log_f.write(string)

log_f = open('SalaryLog.txt', 'a+')
string = str(today)
string += ',\t' + str(Salary_CNY)
string += ',\t' + str(Salary_CNY2USD)
string += ',\t' + str(Salary_USD2NTD)
string += ',\t' + str(ExchangeRate_CNY2USD)
string += ',\t' + str(ExchangeRate_USD2NTD)
string += ',\t' + str(ExchangeRate_CNY2NTD) + '\n'

print(string)
log_f.write(string)
log_f.close()

copyFile('SalaryLog.txt', 'SalaryLog-' + str(today) + '.txt')

if os.path.isfile('..\SalaryLog.txt'):
    copyFile('SalaryLog.txt', '..\SalaryLog.txt')

'''
with open('SalaryLog.txt', 'w+') as log_f:
    string = str(today)
    string += ',\t' + str(Salary_CNY)
    string += ',\t' + str(Salary_CNY2USD)
    string += ',\t' + str(Salary_USD2NTD)
    string += ',\t' + str(ExchangeRate_CNY2USD)
    string += ',\t' + str(ExchangeRate_USD2NTD)
    string += ',\t' + str(ExchangeRate_CNY2NTD) + '\n'
    log_f.write(string)
    print string
log_f.closed
'''
