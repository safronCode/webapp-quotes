from shlex import quote

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Quote


def get_date():
    '''
    Определяем время суток хоста.

    Используется для отображения корректной темы в фронтенде (Утро, ..., Ночь)

    :return:
    day_time (str)
    wish (str)
    '''
    from datetime import datetime

    try:
        current_hour = datetime.now().hour
    except:
        current_hour = 18

    if 5 <= current_hour < 12:
        day_time = 'morning'
        wish = 'Доброго утра'
    elif 12 <= current_hour < 17:
        day_time = 'day'
        wish = 'Доброго дня'

    elif 17 <= current_hour < 22:
        day_time = 'evening'
        wish = 'Доброго вечера'

    else:
        day_time = 'night'
        wish = 'Доброй ночи'

    return day_time, wish

def random_quote():
    '''
        Определяем случайную цитату (в соответствии с весами).

        :return:
        id (int)
    '''
    import random

    quotes = list(Quote.objects.values('id','weight'))
    ids = [q['id'] for q in quotes]
    weights = [q['weight'] for q in quotes]
    selected_id = random.choices(ids, weights, k=1)[0]

    return selected_id


def home_page(request):
    time_theme, wish_message = get_date()

    try:
        quote = Quote.objects.get(id=random_quote())
        quote.views += 1
        quote.save()

    except:
        raise Http404("Хм... Произошла какая-то ошибка\n Tg: @ogPow3r")

    return render(request,template_name='qoutehub/home.html',
                  context={'current_theme': time_theme,
                            'wish_text':wish_message,
                            'quote_text':quote.text,
                            'source':quote.source,
                            'views':quote.views,
                            'likes':quote.likes,
                            'dislikes':quote.dislikes}
                  )

def storage_page(request):
    return HttpResponse('<h1>Storage page</h1>')
