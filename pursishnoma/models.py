from django.db import models

class MainQuestion(models.Model):
    question_main = models.CharField(max_length=200, null = True, blank = True)
    def __str__(self):
        return f"{self.question_main}"    


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    requires_text_response = models.BooleanField(default=False,verbose_name="Добавить текст ввод к вопросу")
    only_text = models.BooleanField(default=False,verbose_name="Только текст")
    question_main = models.ForeignKey(MainQuestion, on_delete= models.CASCADE, null = True, blank = True)
    def __str__(self):
        return f"{self.question_text}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.choice_text}"

class Response(models.Model):
    session_id = models.CharField(max_length=100)  # Идентификатор сессии
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_main = models.ForeignKey(MainQuestion, on_delete = models.CASCADE, blank = True, null = True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    text_response = models.CharField(max_length=200, null=True, blank=True)
    cr_date = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.session_id} -:- {self.ip_address}"
    