# Generated by Django 4.2.3 on 2023-08-02 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_product_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('text', models.TextField()),
                ('rate', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.product')),
            ],
        ),
    ]
