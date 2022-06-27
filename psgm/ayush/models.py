from datetime import datetime
from tkinter import CASCADE
from django.db import models
from datetime import datetime

# Create your models here.
class user_signup(models.Model):
    username=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    type=models.CharField(max_length=20)
    status_user=models.BooleanField(default=False)
    
    class Meta:
        db_table = 'signup'
        managed = True
        verbose_name = 'user_signup'
        verbose_name_plural = 'user_signups'
    # {
    #     "username":"ayusshh19",
    #     "firstname":"Ayush",
    #     "lastname":"Shukla",
    #     "phonenumber":"9892250482",
    #     "email":"ayush.shukla@gmail.com",
    #     "password":"12345678",
    #     "type":"owner"

    # }
    # {
    #         "room_rent": "3000",
    #         "room_description": "All our guestrooms are elegantly furnished with handmade furniture include luxury en-suite facilities with complimentary amenities pack, flat screen LCD TV, tea/coffee making facilities, fan, hairdryer and the finest pure white linen and towels.",
    #         "room_address": "airloli",
    #         "username": "ayusshh18"
    #     }
    # {
    #     "email":"janhavi.shukla@gmail.com",
    #     "password":"87654321"

#     }
# #     {
# "email":"cm.a.20janhavi.chaudhari@gmail.com",
# "password":"ayusshh19"}
# {
# "password":"pbkdf2_sha256$180000$Stuy7XNPUikX$Z0S6QSLcQEmXlldC/lWRZE6lzomrzFWU28FQl09/xvA=",
# "new_password":"ayusshh19",
# "username":"janhavi1907"}
class login_log(models.Model):
    username=models.ForeignKey(user_signup,on_delete=models.CASCADE)
    last_login=models.DateTimeField(auto_now=True)
    login_count=models.IntegerField(default=0)
    last_logout=models.CharField(max_length=100,default='0')
    
    
    class Meta:
        db_table = 'loginlog'
        managed = True
        verbose_name = 'login'
        verbose_name_plural = 'logins'
    
class rooms(models.Model):
    username=models.ForeignKey(user_signup,on_delete=models.CASCADE)
    room_rent=models.CharField(max_length=10)
    room_description=models.CharField(max_length=1000)
    room_address=models.CharField(max_length=100)
    
    class Meta:
        db_table = 'room'
        managed = True
        verbose_name = 'room'
        verbose_name_plural = 'rooms'
        
class password_history(models.Model):
    username=models.ForeignKey(user_signup,on_delete=models.CASCADE)
    password_modified=models.DateTimeField(auto_now=True)
    no_changed=models.IntegerField(default=0)
    
    class Meta:
        db_table = 'history'
        managed = True
        verbose_name = 'his'
        verbose_name_plural = 'hiss'
        
class deleted_account(models.Model):
    username=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    deleted_at=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=20)
    
    class Meta:
        db_table = 'delacc'
        managed = True
        verbose_name = 'del'
        verbose_name_plural = 'dels'
    
    
