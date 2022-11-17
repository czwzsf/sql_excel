from django.db import models


# Create your models here.
class Mis(models.Model):
    """零部件MIS计算"""
    production_code = models.CharField(verbose_name="生产代码", max_length=64, blank=True, null=True)
    chassis_code = models.CharField(verbose_name="底盘码", max_length=64, blank=True, null=True)
    offline_data = models.CharField(verbose_name="下线日期", max_length=16, blank=True, null=True)
    sale_data = models.CharField(verbose_name="销售日期", max_length=16, blank=True, null=True)
    engine_number = models.CharField(verbose_name="发动机码", max_length=32, blank=True, null=True)
    engine_type = models.CharField(verbose_name="发动机型号", max_length=64, blank=True, null=True)
    responsible_organization = models.CharField(verbose_name="责任组织", max_length=32, blank=True, null=True)
    dealer_code = models.CharField(verbose_name="经销商代码", blank=True, null=True, max_length=16)
    dealer_name = models.CharField(verbose_name="经销商名称", blank=True, null=True, max_length=16)
    representative_office_code = models.CharField(verbose_name="商代处代码", blank=True, null=True, max_length=16)
    representative_office_name = models.CharField(verbose_name="商代处名称", blank=True, null=True, max_length=16)
    cluth = models.CharField(verbose_name="离合器", max_length=1280, blank=True, null=True)
    gear_box = models.CharField(verbose_name="变速箱", blank=True, null=True, max_length=6)
    Rear_axle_speed_ratio = models.CharField(verbose_name="后桥速比", max_length=16, blank=True, null=True)
    cage = models.TextField(verbose_name="驾驶室", max_length=1280, blank=True, null=True)
    spread_of_axles = models.CharField(verbose_name="轴距", max_length=32, blank=True, null=True)
    aak_data = models.CharField(verbose_name="aak日期", max_length=32, blank=True, null=True)
