# Generated by Django 5.1.4 on 2024-12-17 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('question_type', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(verbose_name='Описание группы')),
            ],
            options={
                'db_table': 'qna_question_type',
            },
        ),
        migrations.CreateModel(
            name='QuestionAndAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('question_text', models.TextField()),
                ('answer_text', models.TextField(null=True)),
                ('is_answered', models.BooleanField(default=False)),
                ('is_for_publication', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('group_questions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.questiontype')),
            ],
            options={
                'db_table': 'qna_question',
            },
        ),
    ]
