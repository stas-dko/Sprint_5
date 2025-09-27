from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Person
from locators import AuthPageLocators, MainPageLocators, CommonLocators


class AuthHelper:

    @staticmethod
    def wait_for_overlay_to_disappear(driver):
        """Ждем исчезновения модального оверлея, если он есть"""
        try:
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located(CommonLocators.modal_overlay)
            )
        except:
            pass

    @staticmethod
    def login(driver):
        """Вводим данные и кликаем по кнопке логина"""
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )

    @staticmethod
    def assert_login_success(driver):
        """Проверка успешного логина"""
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and order_btn == 'Оформить заказ'
