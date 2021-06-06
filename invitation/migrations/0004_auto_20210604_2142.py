# Generated by Django 3.2.3 on 2021-06-04 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0003_alter_letter_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='id',
        ),
        migrations.AlterField(
            model_name='letter',
            name='code',
            field=models.CharField(default='krmof', max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='unique code'),
        ),
    ]