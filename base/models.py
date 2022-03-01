from pickle import TRUE
from django.db import models

# Create your models here.
# DB 테이블을 생성하는 곳

class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=TRUE, blank=True)   # description은 없어도 된다.