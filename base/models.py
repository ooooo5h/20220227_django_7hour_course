from pickle import TRUE
from django.db import models

# Create your models here.
# DB 테이블을 생성하는 곳

class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=TRUE, blank=True)   # description은 없어도 된다.
    # participants = 
    updated = models.DateTimeField(auto_now=True)  # 업데이트 될때마다 시간이 바뀜
    created = models.DateTimeField(auto_now_add=True)  # 처음에 생성되는 초기값만 저장됨(수정하고 저장해도 값 변경 안됨) 