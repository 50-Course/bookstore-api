# Generated by Django 4.0.7 on 2022-09-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, help_text='Book Title', max_length=100, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, help_text='Tagline', max_length=120, null=True, verbose_name='Subtitle')),
                ('author', models.CharField(max_length=80, verbose_name='Author')),
                ('isbn', models.CharField(max_length=13, verbose_name='ISBN')),
            ],
        ),
    ]
