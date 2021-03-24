import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture()
def setUp(request):
    global driver

    browser = request.config.getoption("browser")

    if browser == 'chrome':

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.maximize_window()

    elif browser == 'firefox':

        driver = webdriver.Firefox(executable_path="D:\\PYTHON\\geckodriver.exe")

        driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')

    outcome = yield

    report = outcome.get_result()

    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":

        xfail = hasattr(report, 'wasxfail')

        if (report.skipped and xfail) or (report.failed and not xfail):

            file = report.nodeid.replace("::", "_") + ".png"

            file_name = 'Screenshots/' + file

            _capture_screenshot(file_name)

            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name

                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_configure(config):
    config._metadata['Project Name'] = 'nopCommerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Ritesh'