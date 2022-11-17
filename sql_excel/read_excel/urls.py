from django.urls import path

from read_excel import views

urlpatterns = [
    # excel文件上传
    path('', views.info),
    # 销售数据上传
    path('upload_excel_sale/', views.upload_excel_sale),
    # 索赔数据上传
    path('upload_excel_claim/', views.upload_excel_claim),
    # 零部件信息上传
    path('upload_excel_parts/', views.upload_excel_parts),
]
