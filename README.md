1. После установки всех зависимостей (requirements) выполнить команду:
```bash
python -m playwright install --with-deps
```
2. Затем можно выполнить запуск тестов:
```bash
pytest --headed
```
3. Запуск тестов с генерацией данных для Allure отчётов:
```bash
pytest --headed --alluredir=reports      
```

<br/>
<br/>
Чтобы пользоваться Allure на Windows, нужно установить Scoop:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```
Затем нужно установить сам Allure через Scoop:
```bash
scoop install allure
allure --version
```
Allure отчёты можно сгенерировать на основе данных, сгенерированных после прогона тестов:
```bash
allure generate reports
```
