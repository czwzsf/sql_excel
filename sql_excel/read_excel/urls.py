from django.urls import path

from read_excel import views

urlpatterns = [
    # excel文件上传
    path('', views.info),
    path('upload_excel/', views.upload_excel)
]
