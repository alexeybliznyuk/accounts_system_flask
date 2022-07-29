# accounts_system_flask
accounts system using:rest api, flask, postgriesql
отвечает на post запросы по /api/reg, /api/login 
принимаю данные в json в формате:
{login: sth, password: sth}
Как запустить: 
1.Создать таблицу в postgresql с помощью create_table.sql
2. Установить все моды из modules
3. Скопировать себе main.py, db.py, config.py
4. Поменять данные в config на свои (сейчас там локал хост)
5. Запустить main.py


Тестовые запросы я делал в server.py
