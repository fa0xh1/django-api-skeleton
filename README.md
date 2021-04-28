<p align="center"><img height="400px" width="100%" src="https://user-images.githubusercontent.com/47023016/116341543-550db380-a80b-11eb-9d11-ec265f6c3e0d.png"></p>

## Introduction

Django Api Skeleton adalah skeleton untuk membangun aplikasi berbasis api/microservice. Tujuan aplikasi ini dibangun untuk memudahkan developer dalam membuat rest api pada django. Karena sudah menyediakan fiture dasar seperti management users,groups,permissions, dan authentication.

# Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Features](#features)
4. [Versions](#versions)
5. [License](#license)

## Requirements

SERVER REQUIREMENTS:

- Python >= 3.6++
- Python PIP

OPTIONAL REQUIREMENTS:

- easy_install
- virtualenv

## Installation

Sebelum menginstall django sebaiknya terlebih dahulu kita menginstall virtualenv dan menggunakannya sebagai environtment kita agar tidak mengganggu modul2 utama yang kita miliki, silahkan ikuti tutorial berikut : [Tutorial Menginstall virtualenv ](https://www.petanikode.com/python-virtualenv/)

Setelah itu ikuti langkah berikut:

1. Jalankan `git clone https://github.com/0xft1h/django-api-skeleton.git`
2. dan setelah itu `cd django-api-skeleton && pip -r requirements.txt`
3. jalankan `./manage.py makemigrations atau python manage.py makemigrations`
4. Kemudian jalankan `./manage.py migrate atau python manage.py migrate`
5. Setelah itu kita jalankan aplikasinya `./manage.py runserver atau python manage.py runserver`
6. Happy hacking!

## Features

# Authentication

![authentication](https://user-images.githubusercontent.com/47023016/116343107-057cb700-a80e-11eb-8fe2-aace16c9697e.png)

# Groups and Permissions management

![group management](https://user-images.githubusercontent.com/47023016/116343159-204f2b80-a80e-11eb-9944-b992694d37da.png)

# Users Management

![users management](https://user-images.githubusercontent.com/47023016/116343321-66a48a80-a80e-11eb-87d2-dad97c726247.png)

# Redoc Documention

![redoc](https://user-images.githubusercontent.com/47023016/116343397-8cca2a80-a80e-11eb-9703-3bc76388b497.png)

## Versions

Apiskeleton 1.0

## License

Django-api-skeleton is now an open-sourced software licensed under the MIT license.
