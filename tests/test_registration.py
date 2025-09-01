# pytest -v --driver Chrome --driver-path C:/chromedriver
# pytest -v --driver Firefox --driver-path C:/gecodriver tests/test_registration.py
import pytest
from pages.rega_page import RegaPage
from generators import generate_test_email, write_data_to_file
import re


@pytest.skip(allow_module_level=True)
# Checking registration process and receiving password on email
def test_registration_successful(web_browser):
    """
    Test successful user registration.
    Steps:
    1. Fill out registration form with valid data.
    2. Verify successful registration message is displayed.
    """
    page = RegaPage(web_browser)
    mail_name, email = generate_test_email()
    username = "Autotestov User Lotikovich"

    try:
        # Fill out the registration form
        page.check_box.scroll_to_element()
        assert page.check_box.is_presented(), "Checkbox is not presented!"
        assert page.agree_with_policy_link.is_clickable(), "Agreement is not clickable!"
        page.user_email.send_keys(email)
        page.user_name.send_keys(username)
        page.user_phone.send_keys("9998884455")
        page.submit_btn.click()

        # Verify successful registration message
        page.successful_rega_msg.wait_to_be_clickable()
        assert page.successful_rega_msg.is_presented(), "Successful registration message not found."
        page.successful_rega_msg.click()

        # Get password by mail
        page.open_new_tab('https://tempmail.plus/ru/#!')
        page.login_name.wait_to_be_clickable()
        page.login_name.clear_by_backspaces()
        page.login_name.send_keys(mail_name)
        page.domain_list.click()
        page.domain_email.click()
        page.copy_button.click()
        page.first_email.wait_to_be_clickable()
        page.first_email.click()
        page.letter_text.scroll_to_element()
        page.wait_page_loaded()
        l_text = page.letter_text.get_text()
        password_pattern = r'\s*([a-zA-Z0-9]+)'
        new_password = re.search(password_pattern, l_text).group(1) if re.search(password_pattern, l_text) else None
        # write_data_to_file(new_password, "tests/files/password.txt")
        page.switch_first_tab()
        page.wait_page_loaded()
        page.password.scroll_to_element()
        page.password.send_keys(new_password)
        page.login_submit_btn.scroll_to_element()
        page.login_submit_btn.click()
        assert page.profile_btn

    except AssertionError as e:
        # Log the error message
        with open(r'C:\Users\chudi\Environments\Lotika\tests\files\log.txt', "a+") as file:
            file.write(f"Test Registration Failed: {str(e)}\n")
        raise e
    finally:
        web_browser.quit()
