# Generated by Django 4.0 on 2021-12-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
