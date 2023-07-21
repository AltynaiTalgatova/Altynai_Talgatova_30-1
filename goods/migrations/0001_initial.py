# Generated by Django 4.2.3 on 2023-07-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('size', models.CharField(max_length=15)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('rate', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]