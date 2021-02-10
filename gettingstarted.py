from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


opts = Options()
#opts.set_headless()
#assert opts.headless # Operating in headless mode
#browser = webdriver.Chrome(executable_path=r'D:\selenium\chromedriver.exe')
browser = Chrome()

opts.add_experimental_option("prefs", { "profile.default_content_setting_values.geolocation": 1})

# SET CAPABILITY
desired_cap = opts.to_capabilities()
desired_cap.update({
  'browser_version': '75.0',
  'os': 'Windows',
  'os_version': '10'
})


browser.get('https://lipa.maps.arcgis.com/apps/CrowdsourceReporter/index.html?appid=b95ccdd8bfa24f45889a3ea4a77dcae7')
sleep(5)
#browser.find_element_by_xpath("//button[@title='Sign in as a guest']").click()
#find_element_by_link_text("Text of Link")
browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div/div[2]/div[1]').click()
print("log in as guest clicked")
sleep(5)
browser.find_element_by_xpath('//*[@id="dijit__WidgetsInTemplateMixin_3"]/div/div[2]/div/div[1]/button').click()
print("x clicked")
sleep(10)
browser.find_element_by_xpath('//*[@id="dijit__WidgetsInTemplateMixin_6"]/div[3]').click()
print("submit new problem clicked")
sleep(10)

##############
# Find id of option 
x = browser.find_element_by_id('category') 
drop = Select(x) 
  
# Select by index 
drop.select_by_index(2) 
############
#browser.find_element_by_xpath("//select[@id='category_label_0']/option[value()='Wire Down']").click()

x = browser.find_element_by_id('probtype') 
drop = Select(x)  
drop.select_by_index(2) 

x = browser.find_element_by_id('Sparking_Burning') 
drop = Select(x)  
drop.select_by_index(2) 

x = browser.find_element_by_id('Tree_Condition') 
drop = Select(x) 
drop.select_by_index(2) 
#details

x = browser.find_element_by_id('details') 
x.send_keys('test selenium simran try one')

x = browser.find_element_by_id('details') 
x.send_keys('1')

x = browser.find_element_by_id('pocfullname') 
x.send_keys('QA')

x = browser.find_element_by_id('pocemail') 
x.send_keys('qa@qa.com')

x = browser.find_element_by_id('pocphone') 
x.send_keys('0000000000')


x = browser.find_element_by_xpath('//*[@id="dijit__WidgetsInTemplateMixin_8"]/div[1]/div/div/div/input').click()
x.send_keys("999 stewart ave bethpage")
#drop = Select(x)
#drop.select_by_index(0)
#driver.find_element_by_css_selector('div.button.c_button.s_button').click()

#browser.find_element_by_xpath('//*[@title="submit"]').click()

sleep(20)
browser.close()



