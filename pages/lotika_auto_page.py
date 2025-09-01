# -*- encoding=utf8 -*-
import os
from pages.base_page import WebPage
from pages.elements import WebElement, ManyWebElements


class LotikaAutoPage(WebPage):
    def __init__(self, web_browser, url=''):
        if not url:
            url = os.getenv("AUTH_URL") or 'https://dev.lotika.ru/auto'
        super().__init__(web_browser, url)

    # Header elements
    prices_menu = WebElement(xpath='//body/div/div/div[1]/div/div/div/ul/li[3]/a')
    help_menu = WebElement(xpath='//body/div/div/div[1]/div/div/div/ul/li[2]/button')
    lots_link = WebElement(css_selector='a[href="/"]')
    sign_in_btn = WebElement(xpath='//body/div/div/div[1]/div/div/div/a/button')
    profile_btn = WebElement(css_selector='')

    # Search VIN or Gosnomer
    search_input_one = WebElement(xpath='//body/div/div/div/div/div/div/div/form/div/div/div/div/input')
    search_input_two = WebElement(xpath='//body/div/div/div[2]/div/div[1]/div/div[4]/form/div/div/div/div/input')
    search_btn = WebElement(xpath='//body/div/div/div/div/div/div/div/form/div/button')
    search_report_balance = WebElement(xpath='//body/div/div/div[2]/div/div[1]/div/div[1]/div[1]/form/h4')

    # Menu elements
    report_example = WebElement(css_selector='a[href="/auto/report/example"]')
    prices_button = WebElement(xpath='//body/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/a[2]')

    # Unauthorized mode: purchase form
    email_redirect_form = WebElement(xpath='//div[2]/div[3]/div')
    email_field = WebElement(css_selector='a[name="email"]')
    agreement_link = WebElement(css_selector='a[href="/service-rules"]')

    # Footer
    offer_link = WebElement(css_selector='')
    privacy_link = WebElement(css_selector='')
    pd_link = WebElement(css_selector='')
    tel_number = WebElement(css_selector='')
    email_link = WebElement(css_selector='')





