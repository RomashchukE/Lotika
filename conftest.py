import uuid
import pytest
from selenium import webdriver

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    ''' This function helps to detect that some test failed
    and pass this information to teardown:'''
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(autouse=True)
def web_browser(request):
    # browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser.maximize_window()

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        # Make screen-shot for local debug:
        browser.save_screenshot('tests/files/' + str(uuid.uuid4()) + '.png')

        # For happy debugging:
        print('URL: ', browser.current_url)
        print('Browser logs:')
        for log in browser.get_log('Firefox'):
            print(log)


