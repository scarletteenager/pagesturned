# Generated by Django 4.1.2 on 2022-11-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_poem_comments_alter_poem_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]