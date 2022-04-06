# Generated by Django 4.0.3 on 2022-03-11 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userId', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_Name', models.CharField(max_length=30)),
                ('last_Name', models.CharField(max_length=30)),
                ('mobile_Number', models.BigIntegerField(unique=True)),
                ('user_Role', models.CharField(max_length=10)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
