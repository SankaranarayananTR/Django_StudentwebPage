# Generated by Django 4.2.9 on 2024-02-04 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_duration', models.CharField(max_length=100)),
                ('course_fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=150)),
                ('stud_phno', models.BigIntegerField()),
                ('stud_mail', models.CharField(max_length=150)),
                ('paid_fees', models.IntegerField()),
                ('pending_fees', models.IntegerField()),
                ('stud_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Studentapp.city')),
                ('stud_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Studentapp.course')),
            ],
        ),
    ]
