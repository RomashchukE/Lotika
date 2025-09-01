# -*- encoding=utf8 -*-
import os
from pages.base_page import WebPage
from pages.elements import WebElement, ManyWebElements


class LotikaAutoTariffsPage(WebPage):
    def __init__(self, web_browser, url=''):
        if not url:
            url = os.getenv("AUTH_URL") or 'https://dev.lotika.ru/auto/tariffs'
        super().__init__(web_browser, url)

    # Header elements
    buy_1_btn = WebElement(xpath='//body/div/div/div[2]/div/div/div[1]/div[1]/button')
    buy_5_btn = WebElement(xpath='//body/div/div/div[1]/div/div/div/ul/li[2]/button')
    buy_10_btn = WebElement(css_selector='a[href="/"]')
    buy_25_btn = WebElement(xpath='//body/div/div/div[1]/div/div/div/a/button')

    confirm_button = WebElement(xpath='//body/div[2]/div[3]/div/div[3]/div/div/button[2]')
    decline_button = WebElement(xpath='//body/div[2]/div[3]/div/div[3]/div/div/button[1]')

    #Yoomoney locators

    pay_by_wallet_link = WebElement(css_selector='a[data-qa-payment-option-preview-type="wallet"]')
    pay_wallet_button = WebElement(css_selector='.MuiButton-root.MuiButton-contained.MuiButton-containedActive.'
                                                'MuiButton-sizeLarge.MuiButton-containedSizeLarge.MuiButton-disableElevation.'
                                                'MuiButton-fullWidth.MuiButtonBase-root.qa-confirm-payment-button.mui-1tpbmmi')
    pay_by_card_link = WebElement(css_selector='a[data-qa-payment-option-preview-type="anyCard"]')

    place_an_order_form = WebElement(xpath='//body/div/div/div[2]/div/div/div[2]/button')



