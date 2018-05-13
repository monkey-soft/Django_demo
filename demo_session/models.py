from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)  # 账号
    password = models.CharField(max_length=20)  # 密码
    nickname = models.CharField(max_length=20)  # 昵称

