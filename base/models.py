from django.db import models


# Create your models here.
# DB 테이블을 생성하는 곳

# class Topic(models.Model):
#     name = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name


# class Room(models.Model):
#     host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)   # description은 없어도 된다.
#     participants = models.ManyToManyField(User, related_name='participants', blank=True)
#     updated = models.DateTimeField(auto_now=True)  # 업데이트 될때마다 시간이 바뀜
#     created = models.DateTimeField(auto_now_add=True)  # 처음에 생성되는 초기값만 저장됨(수정하고 저장해도 값 변경 안됨) 
    
#     class Meta:
#         ordering = ['-updated', '-created']
    
#     def __str__(self):
#         return self.name
    
# class Message(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE) # 누가 부모(ROOM)를 삭제하면, 연결된 모든 메세지도 삭제하자 (CASCADE)
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True) 
#     created = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['-updated', '-created']
    
#     def __str__(self):
#         return self.body[0:50]