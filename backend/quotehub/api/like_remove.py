import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quotehub.models import QuoteLike


@csrf_exempt
@login_required
def like_remove(request):
    quote_id = int(json.loads(request.body).get('quote_id'))
    if not QuoteLike.objects.filter(quote_id=quote_id, user=request.user).exists():
        return JsonResponse({"ok": False})

    QuoteLike.objects.filter(quote_id=quote_id, user=request.user).delete()
    return JsonResponse({"ok": True})
