# Generated by Django 4.2.5 on 2023-11-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_shopuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users_avatars', verbose_name='аватар'),
        ),
    ]
