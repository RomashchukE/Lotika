#pytest -v --driver Chrome --driver-path C:/chromedriver

import pytest
from pages.rega_page import RegaPage
from generators import random_email

#@pytest.skip(allow_module_level=True)
def test_registration_successful(web_browser):
    """
    Test successful user registration.

    Steps:
    1. Fill out registration form with valid data.
    2. Verify successful registration message is displayed.

    """
    page = RegaPage(web_browser)
    email, hashed_email = random_email() #[0]
    username = "Autotest"


    try:
        assert page.user_email.is_presented(), "Email input field not found."
        assert page.user_email_placeholder.is_presented(), "Email placeholder not found."
        #assert page.user_email_placeholder.get_attribute('placeholder') == "Email", "Incorrect email placeholder text."

        assert page.user_phone.is_presented(), "Phone input field not found."
        #assert page.user_phone_placeholder.get_text() == "Телефон", "Incorrect phone placeholder text."

        assert page.user_name.is_presented(), "Username input field not found."
        #assert page.user_name_placeholder.get_text() == "ФИО", "Incorrect username placeholder text."

        # Fill out the registration form
        page.check_box_unmarked.scroll_to_element()
        page.user_email.send_keys(email)
        page.user_name.send_keys(username)
        page.check_box_unmarked.click()
        page.submit_btn.click()

        # Verify successful registration message
        page.successful_rega_msg.wait_to_be_clickable()
        assert page.successful_rega_msg.is_presented(), "Successful registration message not found."

    except AssertionError as e:
        # Log the error message
        with open(r'C:\Users\chudi\Environments\Lotika\tests\files\log.txt', "a+") as file:
            file.write(f"Test Registration Failed: {str(e)}\n")
        raise e
    finally:
        web_browser.quit()
