# Generated by Django 4.0 on 2022-11-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_excel', '0003_claim_data_parts_data_rename_mis_sale_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='lbjmc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_parts', models.CharField(max_length=256, verbose_name='零部件名称')),
            ],
        ),
    ]
