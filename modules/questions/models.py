from django.db import models

class QuestionType(models.Model):
    question_type = models.CharField(primary_key=True, unique=True, max_length=64)
    description = models.TextField(verbose_name="Описание группы")

    def __str__(self):
        return f"{self.question_type}"

    class Meta:
        db_table = "qna_question_type"


class QuestionAndAnswers(models.Model):
    user_email = models.EmailField()
    question_text = models.TextField()
    answer_text = models.TextField(null=True)
    group_questions = models.ForeignKey(QuestionType, on_delete=models.CASCADE, null=True)
    is_answered = models.BooleanField(default=False)
    is_for_publication = models.BooleanField(default=False)  # для публикации на странице часто задаваемых вопросов и ответов
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "qna_question"
