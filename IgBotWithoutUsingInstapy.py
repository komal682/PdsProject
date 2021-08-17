from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# for handling browser notification
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

#Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
"profile.default_content_setting_values.notifications": 1
})



def start_browser_login():
    browser = webdriver.Chrome(chrome_options=option,executable_path='./drivers/chromedriver')
    browser.implicitly_wait(5)

    browser.get('https://www.instagram.com/')

    #login
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys("xxxx")
    password_input.send_keys("1234")

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(5)
    browser.find_element_by_xpath('//button[@type="button"]').click()
    sleep(5)
    browser.find_element_by_css_selector("button.aOOlW:nth-child(1)").click()  #this is included if we had include option or we usig firefox
    sleep(5)




#start of program

start_browser_login()

