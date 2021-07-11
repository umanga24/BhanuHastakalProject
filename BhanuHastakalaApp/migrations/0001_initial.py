# Generated by Django 3.1.7 on 2021-06-28 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(null=True, upload_to='product_image')),
                ('market_price', models.PositiveIntegerField()),
                ('selling_price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('warrenty', models.CharField(blank=True, max_length=100, null=True)),
                ('return_policy', models.CharField(blank=True, max_length=100, null=True)),
                ('review_count', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BhanuHastakalaApp.category')),
            ],
        ),
    ]