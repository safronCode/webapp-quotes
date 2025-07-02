from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Quote


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
    try:
        quote = Quote.objects.get(id=random_quote())
        quote.views += 1
        quote.save()

    except:
        raise Http404("Хм... Произошла какая-то ошибка\n Tg: @ogPow3r")

    initial_data = {
        "quoteId": quote.id,
        "text": quote.text,
        "likes": quote.likes,
        "dislikes": quote.dislikes,
        "views": quote.views,
    }

    return render(request, template_name='index.html', context={"initial_data": initial_data})

def storage_page(request):

    return render(request, template_name='index.html')


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

class SiteLogoutView(LogoutView):
    http_method_names = ["get", "post"]
    template_name = "registration/logout.html"