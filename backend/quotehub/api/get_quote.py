from django.db.models import Count
from django.http import JsonResponse
from quotehub.models import Quote


def get_quote(request):
    quote_id = request.GET.get('quote_id')

    return JsonResponse(Quote.objects.filter(id=quote_id).annotate(like_cnt=Count('quotelike'), dislike_cnt=Count('quotedislike'), view_cnt=Count('quoteview')).values()[0])
