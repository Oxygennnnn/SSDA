# SSDA
This is a Software System Design and Architecture course project: Online Polling System.

The project follows the client-server architecture pattern.

### Project Member
**Li Haoyang 20223802005**;

**Chen Yuchen 20223802061**; 

**Shen Daliang 20223801066**;

**Mo zichong 20223802081**;

**Ding Yuwenqi 20223802087**;

### Code Run
**Update Database**

Before running the system, make sure your database is up-to-date. You can update your database with the following code.
```
python manage.py makemigrations
python manage.py migrate
```

**Create Superuser**

If you want to use administrator rights, run the following code to create an administrator account, then you can log in 
to manage the system.
```
python manage.py createsuperuser
```

**Run Server**

Run the following code to start the server.
```
python manage.py runserver
```