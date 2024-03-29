# Generated by Django 5.0.2 on 2024-02-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Предпросмотр')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'Блоговая запись',
                'verbose_name_plural': 'Блоговые записи',
            },
        ),
    ]
