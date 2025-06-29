from django.db import models

class Quote(models.Model):

    text = models.TextField(max_length=1000, help_text='Текст цитаты')
    source = models.TextField(max_length=150, help_text='Источник, автор')
    weight = models.FloatField(help_text='Вес частоты появления')
    views = models.IntegerField(default=0, help_text='Число просмотров')
    likes = models.IntegerField(default=0, help_text='Число лайков цитаты')
    dislikes = models.IntegerField(default=0, help_text='Число дизлайков цитаты')

    def __str__(self):

        return self.text
