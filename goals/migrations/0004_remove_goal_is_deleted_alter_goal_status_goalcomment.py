# Generated by Django 4.1.4 on 2023-01-08 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0003_alter_goalcategory_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='is_deleted',
        ),
        migrations.AlterField(
            model_name='goal',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'К выполнению'), (2, 'В процессе'), (3, 'Выполнено'), (4, 'Архив')], default=1, verbose_name='status'),
        ),
        migrations.CreateModel(
            name='GoalComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('text', models.TextField(verbose_name='Текст')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goals.goal', verbose_name='Цель')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
