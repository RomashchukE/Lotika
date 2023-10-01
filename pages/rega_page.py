# -*- encoding=utf8 -*-
import os
from pages.base_page import WebPage
from pages.elements import WebElement, ManyWebElements

class RegaPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("AUTH_URL") or 'https://dev.lotika.ru/registration'
        super().__init__(web_driver, url)

    # Registration form
    reg_btn = WebElement(class_name='.sc-jWOkvS.bVkwgs')

    # Input fields of the registration form
    logo_redirect = WebElement(css_selector='a[href="/"]')
    user_email = WebElement(css_selector='[name="email"]')
    user_email_placeholder = WebElement(css_selector='[placeholder="Email"]')
    user_name = WebElement(css_selector='[name="nickname"]')
    user_name_placeholder = WebElement(css_selector='[placeholder="ФИО"]')
    user_phone = WebElement(css_selector='[name="phone"]')
    user_phone_placeholder = WebElement(css_selector='[placeholder="Телефон"]')

    # Another elements of the registration form
    # Placeholder for unimplemented elements:
    # agreement_link = WebElement(css_selector='')

    check_box_unmarked = WebElement(css_selector='label.MuiFormControlLabel-root.jss1 :nth-child(1)')

    submit_btn = WebElement(css_selector='button[type="submit"]')
    submit_btn_disabled = WebElement(css_selector='button[disabled=""]')
    successful_rega_msg = WebElement(xpath="//div[contains(text(), 'Поздравляем')]")
    login_link = WebElement(css_selector='a[href="/login"]')

    # Error messages for the page
    error_empty_email = WebElement(xpath='//div/div[2]/form/div[1]/div[1]/p')
    error_empty_name = WebElement(xpath='//div/div[2]/form/div[3]/div/p')
