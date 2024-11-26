# Generated by Django 3.1 on 2024-11-26 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='图书编号')),
                ('name', models.CharField(max_length=50, verbose_name='书名')),
                ('status', models.BooleanField(default=False, verbose_name='是否出借')),
            ],
            options={
                'verbose_name': '图书表',
                'verbose_name_plural': '图书表',
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_date', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='归还时间')),
                ('s_date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='出借时间')),
                ('name', models.CharField(max_length=20, verbose_name='出借人')),
                ('state', models.BooleanField(default=False, verbose_name='是否归还')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksmanage.books', verbose_name='书籍')),
            ],
            options={
                'verbose_name': '借还记录表',
                'verbose_name_plural': '借还记录表',
                'db_table': 'record',
            },
        ),
    ]
