from django.db import models

class subject(models.Model):
    level1 = models.CharField(max_length=100)
    level2 = models.CharField(max_length=100)
    level3 = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    question_top = models.CharField(max_length=100)
    wave = models.CharField(max_length=100)
    def __str__(self):
        return self.level1+' | '+self.level2+' | ' +self.level3+' | '+self.question
