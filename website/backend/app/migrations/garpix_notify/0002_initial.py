# Generated by Django 3.2.14 on 2022-07-27 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_notify', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifyuserlistparticipant',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_lists', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь (получатель)'),
        ),
        migrations.AddField(
            model_name='notifyuserlistparticipant',
            name='user_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='garpix_notify.notifyuserlist', verbose_name='Список пользователей для рассылки'),
        ),
        migrations.AddField(
            model_name='notifyuserlist',
            name='user_groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Группы пользователей'),
        ),
        migrations.AddField(
            model_name='notifytemplate',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='templates', to='garpix_notify.notifycategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='notifytemplate',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь (получатель)'),
        ),
        migrations.AddField(
            model_name='notifytemplate',
            name='user_lists',
            field=models.ManyToManyField(blank=True, to='garpix_notify.NotifyUserList', verbose_name='Списки пользователей для рассылки'),
        ),
        migrations.AddField(
            model_name='notifyerrorlog',
            name='notify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='garpix_notify.notify', verbose_name='Notify'),
        ),
        migrations.AddField(
            model_name='notify',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifies', to='garpix_notify.notifycategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='notify',
            name='files',
            field=models.ManyToManyField(to='garpix_notify.NotifyFile', verbose_name='Файлы'),
        ),
        migrations.AddField(
            model_name='notify',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifies', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь (получатель)'),
        ),
        migrations.AddField(
            model_name='notify',
            name='users_list',
            field=models.ManyToManyField(blank=True, to='garpix_notify.NotifyUserList', verbose_name='Списки пользователей для рассылки'),
        ),
    ]
