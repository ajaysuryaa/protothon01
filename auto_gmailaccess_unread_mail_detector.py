from selenium import webdriver

bot = webdriver.Chrome(executable_path= "C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
bot.get("http://www.gmail.com")
#for user name
bot.find_element_by_name("identifier").send_keys("ajaysuryaa.19.1@protosem.tech")
bot.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
bot.implicitly_wait(4)
#for password
bot.find_element_by_name("password").send_keys("***")
bot.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
bot.implicitly_wait(10)
#to find number of unread mails
unread = bot.find_element_by_class_name("bsU").text
print("Unread Mails:",unread)