# Generated by Django 3.2.9 on 2021-11-22 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]