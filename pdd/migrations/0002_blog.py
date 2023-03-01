# Generated by Django 3.2 on 2023-02-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='photos/blog')),
            ],
        ),
    ]