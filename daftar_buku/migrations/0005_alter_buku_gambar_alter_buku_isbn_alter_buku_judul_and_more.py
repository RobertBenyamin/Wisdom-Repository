# Generated by Django 5.1 on 2024-08-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_buku', '0004_rating_alter_buku_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='gambar',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='buku',
            name='isbn',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='buku',
            name='judul',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='buku',
            name='kategori',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='buku',
            name='penulis',
            field=models.CharField(),
        ),
    ]
