# Generated by Django 3.2.16 on 2023-02-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20230202_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='logbook_report',
            name='date_of_fault',
            field=models.TextField(default='DD-MM-YYYY'),
        ),
        migrations.AlterField(
            model_name='logbook_report',
            name='driver_email',
            field=models.EmailField(blank=True, default='optional for feeback', max_length=254),
        ),
    ]
