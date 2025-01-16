<h1>Автоматизация тестирования UI и API для учебной платформы <a href="https://stepik.org">Stepik</a></h1>
<img src="source/stepik_main_page.jpg" alt="Стартовая страница Stepik" width="600">

---

### Используемый стек технологий и инструментов

<img src="source/python.png" width="36" height="28"><img src="source/pycharm.png" width="33.5" height="26.5"><img src="source/github.png" width="50" height="26.5"><img src="source/pytest.png" width="33.5" height="26.5"><img src="source/Selenide.png" width="33.5" height="26.5"><img src="source/Selene.png" width="33.5" height="26.5"><img src="source/Allure_Report.svg" width="33.5" height="26.5"><img src="source/Allure_TestOps.svg" width="33.5" height="26.5"><img src="source/Jenkins.svg" width="33.5" height="26.5"><img src="source/Jira.svg" width="33.5" height="26.5"><img src="source/Telegram.svg" width="33.5" height="26.5">
---
## Реализованные автотесты

### UI и API

#### UI

- **Авторизация**
  - ✅ Успешная авторизация в системе и выход из системы
  - ✅ Авторизация с невалидными данными

- **Фильтрация курсов**
  - ✅ Фильтрация курсов "Только с сертификатом"
  - ✅ Фильтрация курсов "Только со скидкой"

- **Поиск**
  - ✅ Проверка успешного поиска на сайте
  - ✅ Проверка неудачного поиска на сайте

#### API

- **Авторизация**
  - ✅ Успешная авторизация в системе
  - ✅ Попытка входа в систему с неверными данными
  - ✅ Выход пользователя из системы

- **Пагинация**
  - ✅ Проверка успешного получения списка курсов
  - ✅ Проверка ответа при запросе несуществующего списка курсов

- **Профиль пользователя**
  - ✅ Проверка получения информации о профиле пользователя
  - ✅ Проверка получения информации о несуществующем профиле пользователя
  - ✅ Проверка обновления информации профиля пользователя


---

### Запуск автотестов

### 💻 Локальный запуск

1. **Склонируйте репозиторий:**
   ```sh
   git clone <git@github.com:lexaeliseev/stepik-ui-api-test-automation.git>
2. **Откройте проект в PyCharm и настройте интерпретатор.**
3. **Установите необходимые библиотеки:**
   ```
   pip install -r requirements.txt
   ```
4. **Создайте и заполните файл .env по образцу в папке проекта:**
   ```python
   URL = "https://stepik.org"
   
   STEPIK_EMAIL = ''
   STEPIK_PASSWORD = ''
   
   SELENOID_URL = 'selenoid.autotests.cloud/wd/hub'
   SELENOID_LOGIN = ''
   SELENOID_PASSWORD = ''
   
   CLIENT_ID = ''
   CLIENT_SECRET = ''
   ```
   
5. **Запустите тесты в PyCharm или в командной строке:**
   ```
   pytest . --browser=[firefox|chrome]
   # Укажите браузер: chrome (по умолчанию) или firefox
   ```
6. **Для генерации отчета о прохождении тестов выполните команду:**
   ```sh
   allure serve allure-results

<h3>
  <img src="source/Jenkins.svg" width="30" height="30" style="vertical-align: middle;">
  Запуск проекта в <a href="https://jenkins.autotests.cloud/job/C16-lexaeliseev-final/">Jenkins</a>
</h3>

1. **Перейдите в раздел "Build with Parameters"**.
2. **Укажите необходимые параметры:**
   - **Адрес удаленного сервера**: Введите URL-адрес удаленного сервера.
   - **Выбор набора тестов**: Укажите, какие тесты должны быть запущены.
   - **Версия браузера**: Выберите версию браузера для тестирования.
   - **Браузер**: Укажите, какой браузер использовать (Chrome или Firefox).
   - **Комментарий для оповещения в Telegram**: Добавьте комментарий, который будет отправлен в Telegram для оповещения о статусе тестов.
3. **Нажмите кнопку "Build" после заполнения всех параметров**.
<img src="source/build_with_parameters.jpg" width="600">

---

<h3>
  <img src="source/Allure_Report.svg" width="30" height="30" style="vertical-align: middle;"> Интеграция с Allure Report
</h3>

**Результаты тестирования доступны в Allure-отчете.**

<img src="source/allure_report_home.jpg" width="600">

**При выполнении автотестов к результатам тестов прикрепляются артефакты, например логи, скриншоты и т.д.**

<img src="source/allure_report_behaviors.jpg" width="600">

**Пример видеозаписи теста (попытка авторизации с невалидными данными)**


<img src="source/auth_failure.gif" width="600">

---

<h3>
  <img src="source/Allure_TestOps.svg" width="30" height="30" style="vertical-align: middle;"> Интеграция с Allure TestOps
</h3>
<img src="source/testops_report.jpg" width="600">

**При выполнении автотестов к результатам тестов прикрепляются артефакты, например логи, скриншоты и т.д.**

---

<h3>
  <img src="source/Jira.svg" width="30" height="30" style="vertical-align: middle;"> Интеграция с Jira
</h3>
<img src="source/jira_report.jpg" width="600">

---

<h3>
  <img src="source/Telegram.svg" width="30" height="30" style="vertical-align: middle;"> Оповещения в Telegram
</h3>

**После выполнения тестов, Telegram-бот уведомляет о результатах тестирования, включая график и информацию о тестовом прогоне.**

<img src="source/telegram_report.jpg" width="600">




