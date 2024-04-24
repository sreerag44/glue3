# Generated by Django 5.0.3 on 2024-04-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbldoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=10, null=True)),
                ('number', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=10, null=True)),
                ('department', models.CharField(max_length=10, null=True)),
                ('educationqualification', models.CharField(max_length=10, null=True)),
                ('experience', models.CharField(max_length=10, null=True)),
                ('drid', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]