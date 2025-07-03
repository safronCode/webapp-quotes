from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from thefuzz import fuzz


class Quote(models.Model):

    text = models.TextField(max_length=550, help_text='Текст цитаты')
    source = models.TextField(max_length=120, help_text='Источник, автор')
    weight = models.FloatField(help_text='Вес частоты появления')


    def clean(self):
        '''Валидация при сохранении новых цитат.

        Если текст новой совпадает (или схож на 90+ %) с одной из сохраненных цитат, вызываем
        ValidationError. Не даём администратору сохранить "дублирующую" цитату.
        '''

        # Приводим текст цитаты к единому виду (+нижний регистр)
        normalized = self.text.strip().lower()
        # Цепляем в рассмотрение все цитаты, кроме текущей
        existing_quotes = Quote.objects.exclude(id=self.id).values_list("text", flat=True)

        # Итерируемся по схожим цитатам в поисках "дублей"
        for q in existing_quotes:
            ratio = fuzz.ratio(normalized, q.strip().lower())
            if ratio > 90:
                raise ValidationError({"text": f"Очень похожая цитата уже есть в базе (Схоже на {ratio}%)."})

    def __str__(self):
        return self.text

class QuoteLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'quote'),)

class QuoteDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'quote'),)

class QuoteView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'quote'),)