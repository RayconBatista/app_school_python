# Generated by Django 2.2.13 on 2021-01-26 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=30)),
                ('nota', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=30)),
                ('questao', models.CharField(max_length=30)),
                ('resposta', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GabaritoAluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao', models.CharField(max_length=30)),
                ('resposta', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.Aluno')),
                ('id_prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.Prova')),
            ],
        ),
        migrations.CreateModel(
            name='Gabarito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao', models.CharField(max_length=30)),
                ('resposta', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.Prova')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='id_prova',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.Prova'),
        ),
    ]