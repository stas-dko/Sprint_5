from data import Person
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators, RecoverPageLocators
from urls import URLS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def wait_for_overlay_to_disappear(self, driver):
        """Ждем исчезновения модального оверлея, если он есть"""
        try:
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
            )
        except:
            pass  # если оверлея нет, продолжаем

    def login(self, driver):
        """Вводим данные и кликаем по кнопке логина"""
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )

    def assert_login_success(self, driver):
        """Проверка успешного логина"""
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        assert driver.current_url == URLS.MAIN_PAGE_URL and order_btn == 'Оформить заказ'

    def test_login_in_login_btn_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        self.wait_for_overlay_to_disappear(driver)
        driver.find_element(*MainPageLocators.login_account_btn).click()
        self.login(driver)
        self.assert_login_success(driver)

    def test_login_in_personal_account_btn_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        self.wait_for_overlay_to_disappear(driver)
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        self.login(driver)
        self.assert_login_success(driver)

    def test_login_in_registration_form_success(self, driver):
        driver.get(URLS.REG_PAGE_URL)
        self.wait_for_overlay_to_disappear(driver)
        driver.find_element(*RegistrationPageLocators.login_account_btn).click()
        self.login(driver)
        self.assert_login_success(driver)

    def test_login_in_recover_form_success(self, driver):
        driver.get(URLS.RECOVER_PAGE_URL)
        self.wait_for_overlay_to_disappear(driver)
        driver.find_element(*RecoverPageLocators.login_account_btn).click()
        self.login(driver)
        self.assert_login_success(driver)