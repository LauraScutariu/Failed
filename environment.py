from utils.webdriver import Webdriver

def before_all(context):
	context.webdriver = Webdriver()

def after_all(context):
	context.webdriver.quit_driver()