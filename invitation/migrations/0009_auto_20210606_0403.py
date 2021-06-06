# Generated by Django 3.2.3 on 2021-06-06 04:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0008_auto_20210606_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='cheering',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='funding',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='code',
            field=models.CharField(default='csivx', max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='unique code'),
        ),
    ]