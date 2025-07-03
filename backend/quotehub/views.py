from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Quote, QuoteLike, QuoteDislike, QuoteView


def home_page(request):
    quote_qs = Quote.objects.order_by('?')

    initial_data = dict.fromkeys(["quoteId", "text", "source", "likes", "dislikes", "views"], None)

    if not quote_qs.exists():
        return render(request, template_name='index.html', context={"initial_data": initial_data})

    quote = quote_qs.first()

    initial_data = {
        "quoteId": quote.id,
        "text": quote.text,
        "source": quote.source,
        "likes": QuoteLike.objects.filter(quote=quote.id).count(),
        "dislikes": QuoteDislike.objects.filter(quote=quote.id).count(),
        "views": QuoteView.objects.filter(quote=quote.id).count(),
    }

    return render(request, template_name='index.html', context={"initial_data": initial_data})


def storage_page(request):

    return render(request, template_name='index.html')


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home-page")

class SiteLogoutView(LogoutView):
    http_method_names = ["get", "post"]
    template_name = "registration/logout.html"