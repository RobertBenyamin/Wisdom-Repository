# Generated by Django 4.2.6 on 2023-10-24 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review_buku', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='posted_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='content',
            new_name='review_text',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='review',
            name='star_count',
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('gambar', models.CharField(max_length=100)),
                ('penulis', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('tahun', models.IntegerField()),
                ('returned', models.BooleanField(default=False)),
                ('borrow_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='buku',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='review_buku.buku'),
            preserve_default=False,
        ),
    ]
