# Generated by Django 4.2.6 on 2024-08-30 20:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_rename_audiofile_instructorrecordings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructorrecordings',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
