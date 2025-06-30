from django.db import models
from django.core.exceptions import ValidationError
from thefuzz import fuzz


class Quote(models.Model):

    text = models.TextField(max_length=550, help_text='Текст цитаты')
    source = models.TextField(max_length=120, help_text='Источник, автор')
    weight = models.FloatField(help_text='Вес частоты появления')
    views = models.IntegerField(default=0, help_text='Число просмотров')
    likes = models.IntegerField(default=0, help_text='Число лайков цитаты')
    dislikes = models.IntegerField(default=0, help_text='Число дизлайков цитаты')

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

    def save(self):
        '''Правило сохранения новой цитаты

        Если у указанного автора >= 3 цитат, то первая из добавленных будет удалена, а текущая добавлена.
        '''

        # Забираем цитаты указанного автора, отсортированного по id (фактически по очереди добавления)
        existing = Quote.objects.filter(source=self.source).order_by('id')
        if self._state.adding and existing.count() >= 3:
            # Определяем и дропаем самую старую запись
            oldest = existing.first()
            oldest.delete()

        super().save()


    def __str__(self):
        return self.text
