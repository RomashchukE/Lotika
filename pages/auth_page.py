# -*- encoding=utf8 -*-
import os
from pages.base_page import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_browser, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://dev.lotika.ru/login'
        super().__init__(web_browser, url)

    # Auth form
    auth_btn = WebElement(class_name='.sc-jWOkvS.iZspci')

    # Input fields of the auth form
    logo_redirect = WebElement(css_selector='a[href="/"]')
    login = WebElement(css_selector='[name="email"]')
    login_placeholder = WebElement(css_selector='[placeholder="Ваш e-mail"]')
    password = WebElement(css_selector='[name="password"]')
    password_placeholder = WebElement(css_selector='[placeholder="Пароль"]')
    show_hide_pswrd = WebElement(css_selector='[aria-label="переключить видимость пароля"]')
    hided_pswrd = WebElement(css_selector='[type="password"]')
    showed_pswrd = WebElement(css_selector='[type="text"]')

    # Another elements of the auth form
    # check_box = WebElement(class_name='')  # Not implemented
    submit_btn = WebElement(css_selector='button[type="submit"]')

    forgot_link = WebElement(css_selector='a[href="/reset-password"]')
    register_link = WebElement(css_selector='a[href="/registration"]')

    profile_btn = WebElement(css_selector='a[href="/user"]')

    # Error messages for pages
    error_empty_login_password = ManyWebElements(class_name='.sc-gFmLcz.kOyrFQ')
