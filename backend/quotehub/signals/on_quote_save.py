from django.db.models.signals import pre_save
from django.db import transaction
from django.dispatch import receiver

from quotehub.models import Quote


@receiver(pre_save, sender=Quote)
def on_quote_save(sender, instance: Quote, **kwargs):
    """
    Перед созданием новой цитаты ограничиваем автора тремя записями.
    • Срабатывает только при _создании_ (instance._state.adding == True)
    • Работает в той же транзакции, что и Save (если она есть)
    """

    # Обновление существующей цитаты пропускаем
    if not instance._state.adding:
        return

    # Оборачиваем в атомарный блок, иначе два параллельных запроса
    # могут одновременно пройти проверку и оставить 4 цитаты
    with transaction.atomic():
        quotes_qs = (
            Quote.objects
            .select_for_update()             # захватываем блокировку на строки
            .filter(source=instance.source)
            .order_by("id")
        )

        if quotes_qs.count() >= 3:
            oldest = quotes_qs.first()
            oldest.delete()