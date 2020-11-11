import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# class URL is passed to this program somehow.
def join_class(url: str, profile: webdriver.FirefoxProfile):	
	browser = webdriver.Firefox(profile)
	browser.get(url)
	
	# handle popup dialog
	WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "push_download_join_by_browser")))
	browser.find_element_by_id("push_download_join_by_browser").click()

	WebDriverWait(browser, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="pbui_iframe"]')))
	
	# Enter name and email, click next
	WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "style-input-2nuAk")))
	name, email = browser.find_elements_by_class_name("style-input-2nuAk")
	name.send_keys("BT18CSE091 Rishikesh") 
	email.send_keys("rishhhhh1357@gmail.com")
	browser.find_element_by_id("guest_next-btn").click()

	# now click ok and join meeting
	try:
		WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Got it")]')))
		browser.find_element_by_xpath('//button[contains(text(), "Got it")]').click()
	except:
		print("Can't find the Got it!")

	try:
		WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Stop video")]')))
		browser.find_element_by_xpath('//button[contains(text(), "Stop video")]').click()
	except:
		print("I think video is off already!")

	try:
		browser.find_element_by_xpath('//button[contains(text(), "Mute")]').click()
	except:
		print("I think it's muted already!")

	try:
		browser.find_element_by_xpath('//button[contains(text(), "Join meeting")]').click()
	except:
		print("GADBAD HAI BRO")

if __name__=='__main__':
	url = sys.argv[-1]
	
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList", 2)
	profile.set_preference("browser.download.manager.showWhenStarting", False)
	profile.set_preference("browser.download.dir", 'C:\\Users\\rishi\\Desktop\\Rish\\Python cool stuff\\Join classes\\useless downloads\\')
	profile.set_preference("browser.download.lastDir", 'C:\\Users\\rishi\\Desktop\\Rish\\Python cool stuff\\Join classes\\useless downloads\\')
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-msdownload, application/octet-stream")
	
	join_class(url, profile)