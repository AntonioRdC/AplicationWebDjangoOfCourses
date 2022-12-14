# Generated by Django 4.1 on 2022-08-10 01:05

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
            name='Assunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=30, verbose_name='Título')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Assunto',
                'verbose_name_plural': 'Assuntos',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=30, verbose_name='Título')),
                ('slug', models.SlugField(max_length=30, verbose_name='Slug')),
                ('desc_geral', models.TextField(verbose_name='Descrição')),
                ('assunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos_assunto', to='cursos.assunto')),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['-criado'],
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=30, verbose_name='Título')),
                ('desc_geral', models.TextField(blank=True, verbose_name='Descrição')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulo_curso', to='cursos.curso')),
            ],
            options={
                'verbose_name': 'Modulo',
                'verbose_name_plural': 'Modulos',
                'ordering': ['titulo'],
            },
        ),
    ]
