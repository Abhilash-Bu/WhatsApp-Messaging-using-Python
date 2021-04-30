from selenium import webdriver
import pywhatkit
import datetime

def whatsApp_selenium(name): # SEND MESSAGE USING SELENIUM LIBRARY

    driver = webdriver.Chrome("chromedriver")
    driver.get("https://web.whatsapp.com/")

    if (input("Enter y after scanning whatsapp web\n") == 'y'):
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
        textbox = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        textbox.send_keys("Hello, For Test purpose only")
        button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
        button.click()

def whatsApp_pywhatkit(number): # SEND MESSAGE USING PYWHATKIT LIBRARY
    time = datetime.datetime.now()
    pywhatkit.sendwhatmsg(number, 'Hi', time.hour, time.minute + 1)


if __name__ == '__main__':

    # TO RUN USING SELENIUM
    name = input("Enter the name of the person to send the message to (NOTE: CASE SENSITIVE)\n")
    whatsApp_selenium(name)

    # TO RUN USING PYWHATKIT
    number = input("Enter number with country code")
    whatsApp_pywhatkit(number)
