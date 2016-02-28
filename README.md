# Django   
Django学习
一、软件环境：python2.7，django1.7.6
二、常用命令：
1、新建工程：django-admin.py startproject project-name
2、新建APP：django-admin.py startapp app-name
3、MYSQL数据库操作：
create database devops default charset utf8 collate utf8_unicode_ci;
FLUSH PRIVILEGES;
4、同步数据库：python manage.py syncdb
注意：Django 1.7.1及以上的版本需要用以下命令
python manage.py makemigrations
python manage.py migrate
5、创建超级管理员：python manage.py createsuperuser
6、服务运行：python manage.py runserver
