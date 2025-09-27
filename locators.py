from selenium.webdriver.common.by import By

# Общие локаторы, используемые на всех страницах
class CommonLocators:
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")

# Локаторы главной страницы
class MainPageLocators:
    main_form = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")
    login_account_btn = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    bun_btn = (By.XPATH, ".//span[text() = 'Булки']")
    sauces_btn = (By.XPATH, ".//span[text() = 'Соусы']")
    toppings_btn = (By.XPATH, ".//span[text() = 'Начинки']")
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    sauces = (By.XPATH, ".//h2[text() = 'Соусы']")
    sauces_ul = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]")
    bun = (By.XPATH, ".//h2[text() = 'Булки']")
    bun_ul = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]")
    topping = (By.XPATH, ".//h2[text() = 'Начинки']")
    topping_ul = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]")

# Локаторы страницы авторизации
class AuthPageLocators:
    auth_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")
    email_input = (By.XPATH, ".//input[@name = 'name']")
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")
    login_account_btn = (By.XPATH, "//button[text() = 'Войти']")
    registration_btn = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    recover_btn = (By.XPATH, "//a[text() = 'Восстановить пароль']")

# Локаторы страницы регистрации
class RegistrationPageLocators:
    name_input = (By.XPATH, "(.//input[@name = 'name'])[1]")
    email_input = (By.XPATH, "(.//input[@name = 'name'])[2]")
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")
    registration_btn = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")
    login_account_btn = (By.XPATH, ".//a[text() = 'Войти']")
    error_message_double_reg = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")
    error_message_incorrect_password = (By.XPATH, ".//p[text() = 'Некорректный пароль']")

# Локаторы страницы восстановления пароля
class RecoverPageLocators:
    email_input = (By.XPATH, ".//label[text() = 'Email']")
    recover_btn = (By.XPATH, ".//button[text() = 'Восстановить']")
    login_account_btn = (By.XPATH, ".//a[text() = 'Войти']")

# Локаторы личного кабинета
class PersonalAreaLocators:
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")
    profile_btn = (By.XPATH, ".//a[text() = 'Профиль']")
    order_history_btn = (By.XPATH, ".//a[text() = 'История заказов']")
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")
    cancel_btn = (By.XPATH, ".//button[text() = 'Отмена']")
