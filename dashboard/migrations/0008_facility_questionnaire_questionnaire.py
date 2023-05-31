# Generated by Django 3.0.5 on 2023-01-12 08:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20221219_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=750)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('number_of_questions', models.IntegerField(default=1)),
                ('active_till', models.DateField(default=datetime.datetime.now)),
                ('target_app', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Questionnaires',
            },
        ),
        migrations.CreateModel(
            name='Facility_Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Questionnaire')),
            ],
            options={
                'db_table': 'Facility_Questionnaire',
            },
        ),
    ]
