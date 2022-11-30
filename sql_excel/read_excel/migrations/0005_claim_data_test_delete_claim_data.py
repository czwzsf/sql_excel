# Generated by Django 4.0 on 2022-11-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_excel', '0004_lbjmc'),
    ]

    operations = [
        migrations.CreateModel(
            name='claim_data_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='生产代码')),
                ('chassis_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='底盘码')),
                ('offline_data', models.CharField(blank=True, max_length=16, null=True, verbose_name='下线日期')),
                ('sale_data', models.CharField(blank=True, max_length=16, null=True, verbose_name='销售日期')),
                ('engine_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='发动机码')),
                ('engine_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='发动机型号')),
                ('responsible_organization', models.CharField(blank=True, max_length=32, null=True, verbose_name='责任组织')),
                ('dealer_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='经销商代码')),
                ('dealer_name', models.CharField(blank=True, max_length=16, null=True, verbose_name='经销商名称')),
                ('representative_office_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='商代处代码')),
                ('representative_office_name', models.CharField(blank=True, max_length=16, null=True, verbose_name='商代处名称')),
                ('cluth', models.CharField(blank=True, max_length=1280, null=True, verbose_name='离合器')),
                ('gear_box', models.CharField(blank=True, max_length=6, null=True, verbose_name='变速箱')),
                ('Rear_axle_speed_ratio', models.CharField(blank=True, max_length=16, null=True, verbose_name='后桥速比')),
                ('cage', models.TextField(blank=True, max_length=1280, null=True, verbose_name='驾驶室')),
                ('spread_of_axles', models.CharField(blank=True, max_length=32, null=True, verbose_name='轴距')),
                ('aak_data', models.CharField(blank=True, max_length=32, null=True, verbose_name='aak日期')),
            ],
        ),
        migrations.DeleteModel(
            name='claim_data',
        ),
    ]
