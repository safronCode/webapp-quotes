from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quotehub.models import QuoteDislike, QuoteLike


@csrf_exempt
@login_required
def dislike_add(request):
    quote_id = request.POST.get('quote_id')
    if QuoteDislike.objects.filter(quote=quote_id, user=request.user).exists():
        return JsonResponse({"ok": False})

    if QuoteLike.objects.filter(quote_=quote_id, user=request.user).exists():
        QuoteLike.objects.filter(quote=quote_id, user=request.user).delete()

    QuoteDislike.objects.create(quote=quote_id, user=request.user)
    return JsonResponse({"ok": True})
