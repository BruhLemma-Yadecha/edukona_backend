# Generated by Django 4.2.6 on 2024-06-24 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_quizsessionstudent_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsessionstudent',
            name='student',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_session_students', to='api.student'),
        ),
    ]
