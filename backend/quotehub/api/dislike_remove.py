from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quotehub.models import QuoteDislike


@csrf_exempt
@login_required
def dislike_remove(request):
    quote_id = request.POST.get('quote_id')
    if not QuoteDislike.objects.filter(quote=quote_id, user=request.user).exists():
        return JsonResponse({"ok": False})

    QuoteDislike.objects.delete(quote=quote_id, user=request.user)
    return JsonResponse({"ok": True})
