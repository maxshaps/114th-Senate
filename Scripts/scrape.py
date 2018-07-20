import os
from sys import argv
from os.path import exists
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


"""
Navigates to a series of webpages on the Voteview website (database maintained
by UCLA Professor Jeffrey Lewis) that downloads all roll call voting data from
the 114th Senate.
Input: numberRollVotes = Number of roll call votes that script needs to collect.
"""


script, numberRollVotes = argv

baseWebpage = "https://voteview.com/api/downloadXLS?ids=RS1140"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 60) #make sure number is in seconds
for index in range(0,int(numberRollVotes)):
    three_digit_str = '%03d' % (index+1)
    currentWebpage = baseWebpage + three_digit_str
    driver.get(currentWebpage) #put the webpage here
    sleep(5)
    while True:
        if os.path.isfile('*.csv.crdownload'):
            sleep(5)
        else:
            break
driver.close()
