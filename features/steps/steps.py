from behave import given, when, then, step
from selenium_test.pages import homepage
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))




@given (u': I launch Oyeroomie url on desktop')
def step(context):
       context.browser.get('https://www.Oyeroomie.com/')
       print("Oyeroomie invoked")


@when(u':  I click on source link')
def step_impl(context):

        home_page = homepage.HomePage(context)
        print("Opened source page")
        home_page.click_source_link(context)

@then(u':  It opens url in headless browser and scraps results')
def step_impl(context):
    next_page = homepage.HomePage(context)
    print("Main source page")
    next_page.oyeroomie_results(context)

