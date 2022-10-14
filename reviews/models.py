from django.db import models

# Create your models here.
class Reviews(models.Model):
    # 리뷰제목
    title = models.CharField(max_length=30)
    content = models.TextField()
    # 영화 이름
    movie_name = models.CharField(max_length=30)
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)