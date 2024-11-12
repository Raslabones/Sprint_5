from selenium.webdriver.common.by import By

# Локатор для поля email
LOGIN_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Локатор для поля пароля
LOGIN_PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

 # Кнопка входа
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button') and text()='Войти']")

# Локаторы для успешной авторизации
PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Кнопка "Оформить заказ"

# Локаторы для страницы личного кабинета
PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "nav a[href*='/account'] p")  # Привязка к уникальной ссылке в навигации
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")  # Кнопка выхода в Личном кабинете

# Локаторы для проверки редиректа
ACCOUNT_PROFILE_URL = "https://stellarburgers.nomoreparties.site/account/profile"
LOGIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/login"

# Локаторы для вкладок в конструкторе
BUNS_TAB = (By.XPATH, "//div[span[text()='Булки']]")  # Вкладка "Булки"
SAUCES_TAB = (By.XPATH, "//div[span[text()='Соусы']]")  # Вкладка "Соусы"
FILLINGS_TAB = (By.XPATH, "//div[span[text()='Начинки']]")  # Вкладка "Начинки"

# Локатор для элемента навигации "Личный кабинет"
NAV_ELEMENT = (By.CSS_SELECTOR, "a[href*='/account']")  # Личный кабинет

# Локатор для логотипа "Stellar Burgers"
LOGO_ELEMENT = (By.CSS_SELECTOR, "a[href='/']")  # Логотип с ссылкой на главную страницу

# Локатор для основного заголовка на главной странице
MAIN_HEADER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")  # Заголовок главной страницы

# Локаторы для страницы восстановления пароля
RECOVERY_LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")  # Кнопка "Войти" на странице восстановления пароля

# Локатор для кнопки входа на странице регистрации
LOGIN_LINK_REGISTRATION_FORM = (By.XPATH, "//a[contains(text(), 'Войти')]")  # Кнопка входа на странице регистрации

# Локатор для кнопки конструктора
CONSTRUCTOR_ELEMENT = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Кнопка конструктора

# Локатор для кнопки "Войти в аккаунт" на главной странице
LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[contains(text(), 'Войти') and contains(@class, 'button')]")  # Кнопка "Войти в аккаунт"

# Локатор для кнопки "Зарегистрироваться"
REGISTRATION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"

# Локаторы для формы регистрации
NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Поле для ввода имени
EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле для ввода email
PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Поле для ввода пароля
REGISTRATION_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"

# Локатор для сообщения об ошибке
ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error.text_type_main-default")  # Сообщение об ошибке