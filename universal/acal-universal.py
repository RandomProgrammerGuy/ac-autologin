from selenium import webdriver

print('Welcome to AC Autologin. \n Please choose your browser first \n \n Use the legend below:\n C = Chrome, F = Firefox, S = Safari')
browserchoice = input('Enter Browser Here')
chromedriver = webdriver.Chrome('chromedriver')
firefoxdriver = webdriver.Firefox('geckodriver')
safaridriver = webdriver.Safari('safaridriver')
if browserchoice == 'C':

elif browserchoice == 'F':

elif browserchoice == 'S':
