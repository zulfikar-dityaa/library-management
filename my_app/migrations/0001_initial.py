# Generated by Django 3.1.1 on 2020-09-13 02:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAdd', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('denda', models.IntegerField(default=10000)),
                ('denda_hilang', models.IntegerField(default=50000)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['-dateAdd'],
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date_in', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_born', models.DateField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
                'ordering': ['-date_in'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_must_back', models.DateField(auto_created=datetime.timedelta(days=7))),
                ('dateAdd', models.DateField(auto_now_add=True)),
                ('date_back_by_member', models.DateField(auto_now_add=True)),
                ('status_denda', models.BooleanField(default=False)),
                ('status_pengembalian', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.member')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Peminjaman',
                'verbose_name_plural': 'Peminjamans',
                'ordering': ['-dateAdd'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.categorie'),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.rating'),
        ),
        migrations.AddField(
            model_name='book',
            name='user_add',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]