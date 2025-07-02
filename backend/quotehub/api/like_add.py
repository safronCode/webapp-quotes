from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from quotehub.models import QuoteLike, QuoteDislike


@csrf_exempt
@login_required
def like_add(request):
    quote_id = request.POST.get('quote_id')
    if QuoteLike.objects.filter(quote=quote_id, user=request.user).exists():
        return JsonResponse({"ok": False})

    if QuoteDislike.objects.filter(quote=quote_id, user=request.user).exists():
        QuoteDislike.objects.filter(quote=quote_id, user=request.user).delete()

    QuoteLike.objects.create(quote=quote_id, user=request.user)
    return JsonResponse({"ok": True})
