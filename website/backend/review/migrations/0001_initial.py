# Generated by Django 3.2.14 on 2022-07-27 15:23

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewListPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'ReviewList',
                'verbose_name_plural': 'ReviewLists',
                'ordering': ('-created_at',),
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='ReviewPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
                ('comment', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Комментарий')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ('-created_at',),
            },
            bases=('garpix_page.basepage',),
        ),
    ]
