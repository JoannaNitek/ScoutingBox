# Generated by Django 2.2.1 on 2019-05-15 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Box', '0004_auto_20190515_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observationform',
            name='scout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='observationlist',
            name='scout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
