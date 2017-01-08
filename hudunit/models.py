from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=25)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    from_player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)

class Answer(models.Model):
    to_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    from_player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    answer_text = models.CharField(max_length=50)
    
    
