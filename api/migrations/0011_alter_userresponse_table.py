# Generated by Django 4.2.6 on 2023-10-30 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_questionmultiplechoice_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userresponse',
            table='api_user_response',
        ),
    ]
