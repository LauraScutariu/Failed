from behave import given, when, then
from pages.login_page import LoginPage

#Scenario: Login successful

@given('I am on the login page')
def step_impl(context):
	context.page = LoginPage()
	context.page.load()

@when('I enter the correct username')
def step_impl(context):
	context.page.set_username(context.config.userdata['valid_username'])
	context.page.set_password(context.config.userdata['valid_password'])

@when('I enter the correct password')
def step_impl(context):
	context.page.set_username(context.config.userdata['valid_username'])
	context.page.set_password(context.config.userdata['valid_password'])

@when('I click the login button')
def step_impl(context):
	context.page.submit_login()

@then('I should be redirected to the my account')
def step_impl(context):
	url_title = context.page.get_url_title()
	assert url_title == "Successful login to your account | Twitter"


#Scenario: Unsuccessful Login(negative username)

@when('I enter the wrong username')
def step_impl(context):
	context.page.set_username(context.config.userdata['invalid_username'])
	context.page.set_password(context.config.userdata['valid_password'])

@then('I should be prompted with an error message')
def step_impl(context):
	url_title = context.page.get_url_title()
	assert url_title == "Error: Login was not successful | Twitter"

#Scenario: Unsuccessful Login(negative password)

@when('I enter the wrong password')
def step_impl(context):
	context.page.set_username(context.config.userdata['valid_username'])
	context.page.set_password(context.config.userdata['invalid_password'])
