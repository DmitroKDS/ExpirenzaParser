from appium import webdriver
from appium.webdriver.client_config import AppiumClientConfig
from appium.options.ios import XCUITestOptions

def start():
    SERVER_URL_BASE = "http://localhost:4723"

    desired_caps = {
        "platformName": "iOS",
        "platformVersion": "18.3.2",
        "deviceName": "iPhone",
        "automationName": "XCUITest",
        "udid": "00008110-000241842651801E",
        "bundleId": "com.ftband.expz",
        "xcodeOrgId": "4BF7UH8B3H",
        "xcodeSigningId": "iPhone Developer",
        "updatedWDABundleId": "com.dmitrokds.WebDriverAgentRunner",
        "webDriverAgentUrl": "http://192.168.31.177:8100",
        "noReset": True,
        "useNewWDA": False,
        "showXcodeLog": True,
    }

    # desired_caps = {
    #     "platformName": "Android",
    #     "platformVersion": "16.0",
    #     "deviceName": "emulator-5554",
    #     "automationName": "UiAutomator2",
    #     "appPackage": "com.ftband.expz",
    #     "appActivity": "com.ftband.expz/com.ftband.expz.main.flow.main.MainActivity",
    #     "noReset": True,
    #     "newCommandTimeout": 300,
    #     "adbExecTimeout": 240000
    # }

    client_config = AppiumClientConfig(
        remote_server_addr=SERVER_URL_BASE,
        direct_connection=True,
        keep_alive=False,
        ignore_certificates=True,
    )

    options = XCUITestOptions().load_capabilities(desired_caps)

    driver = webdriver.Remote(
        options=options,
        client_config=client_config
    )

    return driver