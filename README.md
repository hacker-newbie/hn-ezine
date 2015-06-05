##HN-Community E-Zine (BETA Version)

**Screenshot**
![Index Page](http://s11.postimg.org/3k73h78eb/Screenshot_from_2015_06_05_11_00_01.png "HN E-Zine Index Page")
![Admin Page 1](http://s2.postimg.org/6kkxgiu89/Screenshot_from_2015_06_04_20_43_52.png "HN E-Zine Admin Page 1")
![Admin Page 2](http://s18.postimg.org/4yg8g3ft5/Screenshot_from_2015_06_04_20_43_25.png "HN E-Zine Admin Page 2")

**About**

Ini adalah repositori resmi HN E-Zine CMS (Content Management System). Disini kamu bisa melihat, meng-copy dan berkontribusi langsung dengan project ini.
Stack yand digunakan adalah sbb : 

1. Bahasa : Python
2. Database : PostgreSQL
3. Server : RedHat + Apache
4. Version Controll : Git
5. Front-end : Bootstrap

**Code Tree**

```
.
├── data
├── libs
│   └── openshiftlibs.py
├── openshiftlibs.py
├── README.md
├── requirements.txt
├── setup.py
├── wsgi
│   ├── application
│   ├── myproject
│   │   ├── ezine
│   │   │   ├── admin.py
│   │   │   ├── __init__.py
│   │   │   ├── migrations
│   │   │   │   ├── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   ├── models.py
│   │   │   ├── static
│   │   │   │   ├── css
│   │   │   │   │   ├── hacker.css
│   │   │   │   │   └── rara.css
│   │   │   │   └── img
│   │   │   │       └── python-powered.png
│   │   │   ├── templates
│   │   │   │   └── ezine
│   │   │   │       ├── base.html
│   │   │   │       ├── ezine_detail.html
│   │   │   │       └── ezine_list.html
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   ├── validators.py
│   │   │   └── views.py
│   │   ├── manage.py
│   │   └── myproject
│   │       ├── e-zine
│   │       │   └── txt
│   │       │       └── 2015
│   │       │           └── 06
│   │       │               └── 04
│   │       │                   ├── tes_tHZ2JVS.txt
│   │       │                   └── tes.txt
│   │       ├── __init__.py
│   │       ├── settings.py
│   │       ├── urls.py
│   │       └── wsgi.py
│   ├── README
│   └── static
│       └── README
└── wsgi.py
```

**How To Install**

Saya asumsikan kamu sudah install Python, PIP, Git dan PostgreSQL di mesin kamu. Jika belum, then Google is your friend :)

**Step 1**

Clone project ke localhost :

```
git clone https://github.com/hacker-newbie/hn-ezine.git
```

**Step 2**

Buat database PostgreSQL di local, lalu edit file myproject/myproject/settings.py, dan sesuaikan setting dengan database local kamu.

```
vim wsgi/myproject/myproject/settings.py
```

**Step 3**

Install PostgreSQL Python Adapter dan Django Pyton Web Framework menggunakan PIP

```
pip install psycopg2
pip install django
```

**Step 4**

Masuk ke direktori myproject, dan lakukan migrasi database

```
cd wsgi/myproject
python manage.py makemigrations
python manage.py migrate
python manage.py syncdb
```

**Step 5**

Nyalakan development server

```
python manage.py runserver
```

##To-Do-List

1. Add search
2. Add pagination
3. Add category (Thx to bro Polma)
4. ...

##Greets

Hacker-Newbie Community

##Change-log

=v0.1=
- Initial launch
- Fix static author in template
- Fix some minor bugs



















