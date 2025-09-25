from data import Person, RandomData
from locators import RegistrationPageLocators, AuthPageLocators
from urls import URLS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestRegistrationPage:

    def wait_for_overlay(self, driver):
        """Ждем исчезновения модального оверлея, если он есть"""
        try:
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
            )
        except:
            pass

    def fill_registration_form(self, driver, name, email, password):
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(password)

    def test_registration_success(self, driver):
        driver.get(URLS.REG_PAGE_URL)
        self.wait_for_overlay(driver)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.registration_btn)
        )

        self.fill_registration_form(driver, RandomData.user_name, RandomData.email, RandomData.password)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()

        # Ждем перехода на страницу авторизации
        WebDriverWait(driver, 10).until(lambda d: d.current_url == URLS.AUTH_PAGE_URL)
        login_btn_displayed = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthPageLocators.login_account_btn)
        ).is_displayed()

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed

    def test_registration_incorrect_password_check_error(self, driver):
        driver.get(URLS.REG_PAGE_URL)
        self.wait_for_overlay(driver)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.registration_btn)
        )

        self.fill_registration_form(driver, Person.user_name, Person.email, "12345")
        driver.find_element(*RegistrationPageLocators.registration_btn).click()

        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPageLocators.error_message_incorrect_password)
        ).text

        assert error == 'Некорректный пароль' and driver.current_url == URLS.REG_PAGE_URL

    def test_double_registration_check_error(self, driver):
        driver.get(URLS.REG_PAGE_URL)
        self.wait_for_overlay(driver)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.registration_btn)
        )

        self.fill_registration_form(driver, Person.user_name, Person.email, Person.password)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()

        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPageLocators.error_message_double_reg)
        ).text

        assert error == 'Такой пользователь уже существует' and driver.current_url == URLS.REG_PAGE_URL