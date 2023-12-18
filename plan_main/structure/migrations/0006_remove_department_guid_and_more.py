# Generated by Django 4.2.7 on 2023-12-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0005_merge_20231217_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='guid',
        ),
        migrations.RemoveField(
            model_name='department',
            name='id_department_type',
        ),
        migrations.RemoveField(
            model_name='department',
            name='id_parent_guid',
        ),
        migrations.RemoveField(
            model_name='departmenttype',
            name='guid',
        ),
        migrations.RemoveField(
            model_name='factory',
            name='guid',
        ),
        migrations.AddField(
            model_name='department',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='departmenttype',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='factory',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]