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

import requests
import bs4
import datetime
import os.path
import shutil
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# +++++++++++++++++++++ #
#   Input parameters    #
Salary_CNY = 23000
Salary_USD_Prox = 3600  # 6.388 USD/CNY
logging.disable(logging.DEBUG)
# --------------------- #

if (sys.version_info.major != 3):
    print('This py file only executed on python3')
    raise AssertionError

'''
X_2_NTD_RATE_URL = "http://rate.bot.com.tw"
X_2_NTD_RATE_PAGE = "/Pages/Static/UIP003.zh-TW.htm"

CNY_2_USD_RATE_URL = "www.findrate.tw"
CNY_2_USD_RATE_PAGE = "/converter/CNY/USD/100/"

SEARCH_USD_2_NTD = "美金 (USD)"
SEARCH_CNY_2_NTD = "人民幣 (CNY)"
SEARCH_CNY_2_USD = "1 CNY = "
'''


"2015/08/25"
ExchangeRate_USD2NTD = 32.57000
ExchangeRate_CNY2NTD = 5.00200
ExchangeRate_CNY2USD = 0.1552
ExchangeRate_amount = 0

Salary_CNY2USD = 3600
Salary_CNY2NTD = 118000
Salary_USD2NTD = 118000


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)


def grabExchangeAmount(url):
    global ExchangeRate_amount
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    exchange = soup.select('#content')
    parser_string = str(exchange[0])
    str_start = parser_string.find('<span class="ccOutputRslt">')
    str_start += len('<span class="ccOutputRslt">')
    str_end = str_start + parser_string[str_start:].find('<')
    ExchangeRate_amount = int(parser_string[str_start])
    for chat in range(str_start+1, str_end-2):
        if parser_string[chat] >= '0' and parser_string[chat] <= '9':
            ExchangeRate_amount *= 10
            ExchangeRate_amount += int(parser_string[chat])
    ExchangeRate_amount += int(parser_string[str_end-2]) / 10
    ExchangeRate_amount += int(parser_string[str_end-1]) / 100

'''
Get Current Exchange Rate
USD -> NTD : rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm
CNY -> NTD : rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm
'''

logging.debug('Start Of Program')

today = datetime.date.today()
logging.info(today)

'''
exchangeURL =  "rate.bot.com.tw"
exchangePage = "/Pages/Static/UIP003.zh-TW.htm"
'''

''' Get USD->NTD '''

# Can't find the way to select the nth-of child in beautiful soup with select
# http://stackoverflow.com/questions/24720442/selecting-second-child-in-beautiful-soup-with-soup-select
# Try to parse the row data on #content

# Get CNY->USD
grabExchangeAmount(
    'http://www.x-rates.com/calculator/?from=CNY&to=USD&amount=' +
    str(Salary_CNY)
)
# Salary_CNY2USD = ExchangeRate_amount
# ExchangeRate_CNY2USD = Salary_CNY2USD / Salary_CNY
Salary_CNY2USD = "{0:.1f}".format(ExchangeRate_amount)
ExchangeRate_CNY2USD = "{0:.3f}".format(ExchangeRate_amount / Salary_CNY)
logging.info(
    '[Get ratio] CNY to USD\t %s \t %s'
    % (Salary_CNY2USD, ExchangeRate_CNY2USD)
)

# Get CNY->NTD
grabExchangeAmount(
    'http://www.x-rates.com/calculator/?from=CNY&to=TWD&amount=' +
    str(Salary_CNY)
)

# Salary_CNY2NTD = ExchangeRate_amount
# ExchangeRate_CNY2NTD = Salary_CNY2NTD / Salary_CNY
Salary_CNY2NTD = "{0:.2f}".format(ExchangeRate_amount)
ExchangeRate_CNY2NTD = "{0:.3f}".format(ExchangeRate_amount / Salary_CNY)
logging.info(
    '[Get ratio] CNY to NTD\t %s \t %s'
    % (Salary_CNY2NTD, ExchangeRate_CNY2NTD)
)

# Get Prox USD -> NTD
grabExchangeAmount(
    'http://www.x-rates.com/calculator/?from=USD&to=TWD&amount=' +
    str(Salary_USD_Prox)
)

# Salary_USD2NTD = ExchangeRate_amount
# ExchangeRate_USD2NTD = Salary_USD2NTD / Salary_USD_Prox
Salary_USD2NTD = "{0:.2f}".format(ExchangeRate_amount)
ExchangeRate_USD2NTD = "{0:.3f}".format(ExchangeRate_amount / Salary_USD_Prox)
logging.info(
    '[Get ratio] USD to NTD (prox)\t %s \t %s'
    % (Salary_USD2NTD, ExchangeRate_USD2NTD)
)

"2015/07/01"
'''
ExchangeRate_USD2NTD = 30.86000
ExchangeRate_CNY2NTD = 4.95700
ExchangeRate_CNY2USD = 0.1615
'''

''' Log the Salary_CNY2USD / Salary_USD2NTD into file '''
''' DATE,	CNY_SALARY,	TO_USD,	TO_NTD,	CNY2USD,	USD2NTD,	CNY2NTD '''

if os.path.isfile('SalaryLog.txt'):
    logging.info('Found log file on folder')
else:
    logging.error('Can\'t found log file on folder')
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

logging.info(string)
log_f.write(string)
log_f.close()

copyFile('SalaryLog.txt', 'SalaryLog-' + str(today) + '.txt')

if os.path.isfile('..\SalaryLog.txt'):
    copyFile('SalaryLog.txt', '..\SalaryLog.txt')

logging.debug('End Of Program')
