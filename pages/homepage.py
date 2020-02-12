from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage(object):

    def __init__(self, context):
        context = context

    def click_source_link(self, context):
        print("click_source_link started")

        source_link = context.browser.find_element(By.PARTIAL_LINK_TEXT, 'Roommate Search').click()
        select_roomie = context.browser.get('https://www.Oyeroomie.com/')
        print("It worked")

    def oyeroomie_results(self, context):
        print("OyeRoomie results started")
        rooms = context.browser.find_elements_by_partial_link_text("rooms")
        i = len(rooms)
        print(i)
        cur_win = context.browser.current_window_handle  # get current/main window
        for link in rooms:
            link.click()
            context.browser.switch_to.window(
                [win for win in context.browser.window_handles if win != cur_win][0])  # switch to new window
            mails = context.browser.find_elements_by_xpath("//td[contains(text(),'com')]")
            for mail in mails:
                print(mail.text)
            context.browser.close()  # close new window
            context.browser.switch_to.window(cur_win)  # switch back to main window


