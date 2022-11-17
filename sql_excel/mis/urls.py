from django.urls import path

from read_excel import views

urlpatterns = [
    # mis基础界面
    path('', views.info),
]
