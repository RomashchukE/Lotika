#pytest -v --driver Chrome --driver-path C:/chromedriver

import pytest
from pages.auth_page import AuthPage

def test_successful_auth(web_browser):
    """
    Test successful user sign in.

    Steps:
    1. Fill out auth form with valid data.
    2. Verify successful profile button is displayed.

    """
    page = AuthPage(web_browser)

    try:
        page.login.wait_to_be_clickable()
        assert page.forgot_link.is_presented()
        assert page.register_link.is_presented()
        page.login.send_keys('shumak@gmail.com')
        page.password.send_keys('123456')
        page.submit_btn.click()
        page.profile_btn.wait_to_be_clickable()
        assert page.profile_btn.is_presented()

    except AssertionError as e:
        # Log the error message
        with open(r'C:\Users\chudi\Environments\Lotika\tests\files\log.txt', "a+") as file:
            file.write(f"Test Auth Failed: {str(e)}\n")
        raise e
    finally:
        web_browser.quit()
