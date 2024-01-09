# -*- encoding=utf8 -*-
import os
from pages.base_page import WebPage
from pages.elements import WebElement


class RegaPage(WebPage):
    def __init__(self, web_browser, url=''):
        if not url:
            url = os.getenv("AUTH_URL") or 'https://dev.lotika.ru/registration'
        super().__init__(web_browser, url)

    # Registration form
    reg_btn = WebElement(class_name='.sc-jWOkvS.bVkwgs')

    # Input fields of the registration form
    logo_redirect = WebElement(css_selector='a[href="/"]')
    user_email = WebElement(css_selector='[name="email"]')
    user_name = WebElement(css_selector='[name="nickname"]')
    user_phone = WebElement(css_selector='[name="phone"]')
    check_box = WebElement(css_selector='input[type="checkbox"]')
    agree_with_policy_link = WebElement(css_selector='a[href="/service-rules"]')
    submit_btn = WebElement(css_selector='button[type="submit"]')
    successful_rega_msg = WebElement(xpath="//div[contains(text(), 'Поздравляем')]")
    login_link = WebElement(css_selector='a[href="/login"]')

    # Error messages and disabled elements
    error_empty_email = WebElement(xpath='//div/div[2]/form/div[1]/div[1]/p')
    error_empty_name = WebElement(xpath='//div/div[2]/form/div[3]/div/p')
    #wrong_phone_number = WebElement(xpath='')
    submit_btn_disabled = WebElement(css_selector='button[disabled=""]')

    # TEMP_MAIL locators
    login_name = WebElement(css_selector='#pre_button')
    domain_list = WebElement(css_selector='#domain')
    domain_email = WebElement(xpath='//form[@id="pre_form"]/div/div[2]/div/button[8]')
    copy_button = WebElement(css_selector='button#pre_copy')
    empty_mails_list = WebElement(css_selector='span[data-tr="waiting_for_emails"]')
    first_email = WebElement(css_selector='div.inbox div.mail:nth-child(2)')
    second_email = WebElement(css_selector='div.inbox div.mail:nth-child(3)')
    letter_text = WebElement(css_selector='tbody tbody tr:nth-child(2) td')
    attachments = WebElement(css_selector='.row.no-gutters.attachments div a')
    back_to_list_btn = WebElement(css_selector='#back')

    # Login locators
    password = WebElement(css_selector='[name="password"]')
    login_submit_btn = WebElement(css_selector='button[type="submit"]')
    profile_btn = WebElement(css_selector='a[href="/user"]')
