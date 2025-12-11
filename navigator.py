from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

def tap(driver, text):
    try:
        element = driver.find_element(AppiumBy.IOS_PREDICATE, f'label == "{text}" OR name == "{text}"')
        element.click()
        return True
    except NoSuchElementException:
        print(f"Element '{text}' not found")
        return False



def tap_android(driver, text: None|str = None, resource_id: None|str = None) -> bool:
    try:
        if text is not None:
            element = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{text}")'
            )
            element.click()
        elif resource_id is not None:
            element = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("{resource_id}")'
            )
            element.click()
        return True
    except NoSuchElementException:
        print(f"Element with text '{text}' or resource-id '{resource_id}' not found")
        return False