from urls import URLS
from locators import MainPageLocators, RegistrationPageLocators, RecoverPageLocators
from helpers.auth_helpers import AuthHelper


class TestLogin:

    def test_login_in_login_btn_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        AuthHelper.wait_for_overlay_to_disappear(driver)
        driver.find_element(*MainPageLocators.login_account_btn).click()
        AuthHelper.login(driver)
        AuthHelper.assert_login_success(driver)

    def test_login_in_personal_account_btn_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        AuthHelper.wait_for_overlay_to_disappear(driver)
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        AuthHelper.login(driver)
        AuthHelper.assert_login_success(driver)

    def test_login_in_registration_form_success(self, driver):
        driver.get(URLS.REG_PAGE_URL)
        AuthHelper.wait_for_overlay_to_disappear(driver)
        driver.find_element(*RegistrationPageLocators.login_account_btn).click()
        AuthHelper.login(driver)
        AuthHelper.assert_login_success(driver)

    def test_login_in_recover_form_success(self, driver):
        driver.get(URLS.RECOVER_PAGE_URL)
        AuthHelper.wait_for_overlay_to_disappear(driver)
        driver.find_element(*RecoverPageLocators.login_account_btn).click()
        AuthHelper.login(driver)
        AuthHelper.assert_login_success(driver)
