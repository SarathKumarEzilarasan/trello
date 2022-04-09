import json
import os
import pytest
from from_root import from_root
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None
settings = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--env", action="store", default="local")


def pytest_configure(config):
    global settings
    settings = get_config(config.getoption("--env"))


# Fixtures
@pytest.fixture(scope='session')
def browser(request):
    # pdb.set_trace()
    browser_name = request.config.getoption("browser_name")
    global driver
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def context():
    return {}


def get_config(env):
    file = None
    if str(env).lower() == "local":
        file = "conf_local.json"
    elif str(env).lower() == "dev":
        file = "conf_dev.json"
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config/' + file)) as f:
        _settings = json.load(f)
    return _settings

#
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.option.htmlpath = '/path/to/report.html'


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        isFail = hasattr(report, 'wasxfail')
        if (report.skipped and isFail) or (report.failed and not isFail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            if str(file_name).__contains__("tests/"):
                tmp = str(file_name).split("/")
                file_name = tmp[2]
            path = _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    path = str(from_root('screenshots')) + "/" + name
    driver.save_screenshot(path)
    return path
