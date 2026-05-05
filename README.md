# Django Shop

Интернет-магазин на Django — учебный проект.

## Технологии
- Python 3.12+
- Django 5.x
- PostgreSQL
- Bootstrap 5
- Pillow (для работы с изображениями)

## Функциональность
- ✅ Главная страница
- ✅ Страница контактов с формой обратной связи
- ✅ Админ-панель для управления категориями и продуктами
- ✅ PostgreSQL в качестве базы данных
- ✅ Фикстуры для экспорта/импорта данных
- ✅ Кастомная команда `load_test_data` для загрузки тестовых данных

## Запуск проекта

1. Клонировать репозиторий
```bash
git clone https://github.com/bezza8418/django_shop.git
cd django_shop
```
2. Создать и активировать виртуальное окружение
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```
3. Установить зависимости
```bash
pip install -r requirements.txt
```
4. Настроить переменные окружения
* Создай файл .env в корне проекта:
```
env
DB_NAME=django_shop
DB_USER=postgres
DB_PASSWORD=твой_пароль
DB_HOST=localhost
DB_PORT=5432
```
5. Создать базу данных PostgreSQL
```sql
CREATE DATABASE django_shop;
```
6. Применить миграции
```bash
python manage.py migrate
```
7. Создать суперпользователя
```bash
python manage.py createsuperuser
```
8. Загрузить тестовые данные (опционально)
```bash
python manage.py load_test_data
```
9. Запустить сервер
```bash
python manage.py runserver
```
## Доступные страницы
Главная: http://127.0.0.1:8000/

Контакты: http://127.0.0.1:8000/contacts/

Админка: http://127.0.0.1:8000/admin/

## Структура проекта
```text
django_shop/
├── catalog/                 # Основное приложение
│   ├── fixtures/            # JSON-фикстуры
│   ├── management/          # Кастомные команды
│   │   └── commands/
│   │       └── load_test_data.py
│   ├── migrations/          # Миграции БД
│   ├── templates/           # HTML-шаблоны
│   ├── admin.py             # Настройка админки
│   ├── models.py            # Модели Category и Product
│   ├── urls.py              # Маршруты приложения
│   └── views.py             # Контроллеры
├── shop/                    # Настройки проекта
│   ├── settings.py          # Конфигурация
│   └── urls.py              # Главные маршруты
├── screenshots/             # Скриншоты для ДЗ
├── .env                     # Переменные окружения (не коммитится)
├── .gitignore
├── manage.py
└── requirements.txt
```

## 📄 Лицензия
Проект разработан в учебных целях.

## 📞 Контакты
Автор: bezza8418
