from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Webdriver:
	def __int__(self):
		self.driver = webdriver.Chrome(
			service=Service(ChromeDriverManager().install())
		)
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)

	def quit(self):
		self.driver.quit()