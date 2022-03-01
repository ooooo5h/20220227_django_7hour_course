from django.db import models

# Create your models here.
# DB 테이블을 생성하는 곳

class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)   # description은 없어도 된다.
    # participants = 
    updated = models.DateTimeField(auto_now=True)  # 업데이트 될때마다 시간이 바뀜
    created = models.DateTimeField(auto_now_add=True)  # 처음에 생성되는 초기값만 저장됨(수정하고 저장해도 값 변경 안됨) 
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    # user =
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # 누가 부모(ROOM)를 삭제하면, 연결된 모든 메세지도 삭제하자 (CASCADE)