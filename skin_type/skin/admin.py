from django.contrib import admin
from .models import Comment

#admin page로 데이터모델 조작하기
# Register your models here.
#
# from .models import
# admin.site.register(Post)
admin.site.register(Comment)
