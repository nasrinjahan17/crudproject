# Generated by Django 3.2.4 on 2021-06-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_no',
            field=models.CharField(max_length=40, null=True),
        ),
    ]