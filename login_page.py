import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.webdriver import Webdriver


class LoginPage(Webdriver):
	def load(self):
		self.driver.get('https://twitter.com/i/flow/login')

	def set_username(self, username):   ##username_textbox = self.driver.find_element(By.XPATH, '')
		username_textbox = WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'))
		username_textbox.send_keys(username)

	def set_password(self, password):
		password_textbox = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
		password_textbox.send_keys(password)

	def submit_login(self):
		submit_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
		submit_button.click()