# Бэкэнд небольшого приложение с использование Redis и Mongo

Для запуска надо:
  * Склонировать репозиторий.
  * В папке с кодом выполнить docker-compose up -d (Это запустит монго и редис)
  * Далее выполнить ./manage.py migrate, ./manage.py createsuperuser, ./manage.py runserver
 
 Доп.информация:
   * Для кэширования используется cacheops https://github.com/Suor/django-cacheops
