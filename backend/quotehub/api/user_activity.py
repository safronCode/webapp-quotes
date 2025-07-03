from django.http import JsonResponse
from quotehub.models import QuoteLike, QuoteDislike, QuoteView


def user_activity(request):
    user = request.user
    quote_id = int(request.GET.get('quote_id'))

    is_liked = QuoteLike.objects.filter(user=user, quote_id=quote_id).exists()
    is_disliked = QuoteDislike.objects.filter(user=user, quote_id=quote_id).exists()
    is_view = QuoteView.objects.filter(user=user, quote_id=quote_id).exists()

    return JsonResponse({'isLiked': is_liked, 'isDisliked': is_disliked, 'isView': is_view})