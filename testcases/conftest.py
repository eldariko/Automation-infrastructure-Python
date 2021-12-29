import mysql.connector
import pytest
import requests
from _pytest.fixtures import FixtureRequest
from applitools.selenium import ClassicRunner, Eyes
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.common_ops import get_data
from utils.managers.listeners import EventListener
# ----------------------------------------
# WEB
from utils.managers.manage_pages import ManagePages

# WEB
driver: EventFiringWebDriver
wait: WebDriverWait
action = None
e_driver: WebDriver
db = None

# ----------------------------------------
# MOBILE
reportDirectory = get_data("Reports")
reportFormat = get_data("Xml")
dc = {}
testName = get_data("Untitled")

# ----------------------------------------
# ELECTRON
electron_app = r"C:\Automation\Electrons\Electron API Demos.exe"
edriver = r"..\drivers\electrondriver.exe"


# ----------------------------------------

@pytest.fixture(scope='class')
def my_web_starter(request: FixtureRequest):
    global driver, wait, e_driver
    if get_data("Browser") == "chrome":
        e_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif get_data("Browser") == "edge":
        e_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif get_data("Browser") == "firefox":
        e_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        e_driver = None
        print("Wrong input, unrecognized browser")
    driver = EventFiringWebDriver(e_driver, EventListener())
    driver.maximize_window()
    driver.implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = globals()['driver']
    wait = WebDriverWait(driver, 10)
    globals()['wait'] = wait
    ManagePages.init_web_pages(driver)
    yield driver

    # driver.quit()


@pytest.fixture(scope='function')
def my_web_before_method():
    global driver
    driver.get("http://localhost:4000")


@pytest.fixture(scope="module")
def db_set_up():
    global db
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )
    mycursor = db.cursor()
    mycursor.execute("DROP SCHEMA IF EXISTS users;")
    mycursor.execute("CREATE DATABASE users")
    mycursor.execute(
        "CREATE TABLE if not exists `users`.`user` (`username` VARCHAR(32) NOT NULL,`password` VARCHAR(32) NOT NULL,"
        "`expected` VARCHAR(32) NOT NULL);")
    sql = "INSERT INTO `users`.`user` (`username`,`password`,`expected`)VALUES(%s,%s,%s);"
    val = ("Katharina_Bernier", "s3cret", "@Katharina_Bernier")
    mycursor.execute(sql, val)
    db.commit()


@pytest.fixture(scope='class')
def my_mobile_starter(request):
    global pay_off_calc_page, wait
    dc['reportDirectory'] = reportDirectory
    dc['reportFormat'] = reportFormat
    dc['testName'] = testName
    dc['udid'] = get_data("Udid")
    dc['appPackage'] = get_data('AppPackage')
    dc['appActivity'] = get_data('AppActivity')
    dc['platformName'] = get_data('PlatformName')
    edriver = webdriver.Remote(get_data("LocalHost"), dc)
    driver = EventFiringWebDriver(edriver, EventListener())
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)

    globals()['driver'] = driver
    request.cls.driver = driver
    ManagePages.init_mobile_pages(driver)

    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_api(request):
    # url = get_data("base_url")
    url = 'http://localhost:3000'
    request.cls.url = url


@pytest.fixture(scope='class')
def my_desktop_starter(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    driver.implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = driver
    wait = WebDriverWait(driver, 10)
    globals()['wait'] = wait
    ManagePages.init_desktop_page(driver)
    yield
    driver.quit()


@pytest.fixture(scope='class')
def my_electron_starter(request):
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    driver.implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = driver
    ManagePages.init_electron_page(driver)
    yield
    driver.quit()


@pytest.fixture(name="runner", scope="session")
def runner_setup():
    """
    One test runner for all tests. Print test results in the end of execution.
    """
    runner = ClassicRunner()
    yield runner


@pytest.fixture(name="eyes")
def applitools_set_up(runner):
    global driver, e_driver
    eyes = Eyes(runner)
    eyes.api_key = "Y7YclUHy7uKAB110GYMAC9bTPBHimPnc3wUQ4UyPgBtRs110"
    eyes.open(e_driver, "Hack", "Dismiss test")
    yield eyes
