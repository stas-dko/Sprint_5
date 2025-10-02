import re
from data import RandomData


class TestRandomData:

    def test_random_email_and_password_generation(self):
        """Проверка генерации валидных e-mail и пароля"""

        email_1 = RandomData.email
        password_1 = RandomData.password

        from data import RandomData as RandomData2
        email_2 = RandomData2.email
        password_2 = RandomData2.password

        # --- Проверка e-mail ---
        assert '@' in email_1 and email_1.endswith('yandex.ru'), "Неверный формат e-mail"
        assert '@' in email_2 and email_2.endswith('yandex.ru'), "Неверный формат e-mail"
        assert email_1 != email_2, "Сгенерированные e-mail должны быть уникальными"

        # --- Проверка пароля ---
        for pwd in (password_1, password_2):
            assert len(pwd) >= 6, "Пароль должен быть не короче 6 символов"
            assert re.search(r'\d', pwd), "Пароль должен содержать цифру"
            assert re.search(r'[A-Za-z]', pwd), "Пароль должен содержать букву"