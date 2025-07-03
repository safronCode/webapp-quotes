from django.db.models import Count
from django.http import JsonResponse

from quotehub.models import Quote, QuoteLike, QuoteDislike, QuoteView

def quote_list(request):
    quote_list = (Quote.objects.annotate(like_cnt=Count('quotelike'), dislike_cnt=Count('quotedislike'), view_cnt=Count('quoteview')).order_by('-like_cnt')[:10])
    most_liked_quotes = {}

    for quote in quote_list.values():
        most_liked_quotes[quote.get('id')] = quote
        most_liked_quotes[quote.get('id')]['user_is_liked'] = QuoteLike.objects.filter(quote_id=quote.get('id')).exists()
        most_liked_quotes[quote.get('id')]['user_is_disliked'] = QuoteDislike.objects.filter(quote_id=quote.get('id')).exists()
        most_liked_quotes[quote.get('id')]['user_is_viewed'] = QuoteDislike.objects.filter(quote_id=quote.get('id')).exists()

    return JsonResponse(most_liked_quotes)
