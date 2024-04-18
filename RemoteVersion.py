from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors=yes')

remoteDriver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)