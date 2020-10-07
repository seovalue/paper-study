from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length = 100) # 영화명
    genre = models.CharField(max_length = 100) # 장르
    cast = models.CharField(max_length = 300) # 캐스팅목록
    director = models.CharField(max_length=100) #감독
    vote = models.FloatField()  # 평점
    summary = models.CharField(max_length = 10000) #줄거리
