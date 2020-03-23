# Бэкэнд небольшого приложения с использование Redis и Mongo

Для запуска надо:
  * Склонировать репозиторий.
  * Выполнить следующие команды:
    - python3.8 -m venv venv 
    - source venv/bin/activate
    - pip install -r requirements.txt
    - sudo docker run --name redis-instance --rm -d -p 6379:6379 redis:5.0.7 redis-server --appendonly yes
    - sudo docker run --name mongo-instance --rm -d -p "27017:27017" mongo:4.2.3
    - ./manage.py migrate 
    - ./manage.py createsuperuser 
    - ./manage.py runserver
 
 Доп.информация:
   * Для кэширования используется cacheops https://github.com/Suor/django-cacheops
 
