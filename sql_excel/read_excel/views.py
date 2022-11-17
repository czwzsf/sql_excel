from django import forms
from django.shortcuts import render, HttpResponse, redirect
from openpyxl.reader.excel import load_workbook

from read_excel import models


# Create your views here.
class mis_form(forms.ModelForm):
    class Meta:
        model = models.Mis
        fields = "__all__"


def upload_excel(request):
    """基于Excel的文件上传"""
    # 1. 获取用户上传的文件对象
    form = mis_form(data=request.POST, files=request.FILES)
    file_object = request.FILES.get("filename", None)
    if not file_object:
        return HttpResponse("没有文件可供上传")
    # 2. 将文件对象传递给openpyxl，由openpyxl来进行读取
    wb = load_workbook(file_object)
    # 3. 将读取出来的第一个表格传入到sheet里面
    sheet = wb.worksheets[0]
    dict_list = []
    for row in sheet.iter_rows(min_row=2):
        for item in range(len(row)):
            text = str(row[item].value)
            dict_list.append(text)
        models.Mis.objects.create(production_code=dict_list[1], chassis_code=dict_list[2], offline_data=dict_list[3],
                                  sale_data=dict_list[4], engine_number=dict_list[5], engine_type=dict_list[6],
                                  responsible_organization=dict_list[7], dealer_code=dict_list[8],
                                  dealer_name=dict_list[9], representative_office_code=dict_list[10],
                                  representative_office_name=dict_list[11], cluth=dict_list[12], gear_box=dict_list[13],
                                  Rear_axle_speed_ratio=dict_list[14], cage=dict_list[15],
                                  spread_of_axles=dict_list[16],
                                  aak_data=dict_list[17])
        dict_list.clear()
        # if form.is_valid():
        #     form.save()
    return render(request, 'html/reda_excel.html')


def info(request):
    if request.method == "GET":
        return render(request, 'html/reda_excel.html')
    return render(request, 'html/reda_excel.html')
