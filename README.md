# Django application for selling gift products
This application is created so that the products which generally comes under the category of 'gift items' or 'decorations' can be sold online. The data for the product items were obtained from kaggle in the link:https://www.kaggle.com/datasets/carrie1/ecommerce-data .
It is modelled after the popular ecommerce website 'amazon'. Users can create accounts and add products to their cart. It has the default django admin portal to manage the database and users.

## Apps

In this project multiple apps are created to handle each aspect of the website. They are 'giftzone', 'store', and 'users'.


## Tables
For displaying products and categories, two tables with the same name are created with categories being the common attribute among them. The attribute 'category' is the foreign key for 'Products' table.
Used faker to generate fake descriptioin.
## Requirements
To run the application, use the following command so that all the requirements will be installed to the virtual environment.

            pip install -r requirements.txt

## Create superuser
Creating a superuser lets you handle the admin portal for the django app. Follow the below command to do that.

            python manage.py createsuperuser

## Admin login

The login details for admin access is as follows:
username:alex
password:akvrksgift


## Deployment

The application is deployed on render, a cloud hosting platform. Application URL:https://giftzone-service.onrender.com