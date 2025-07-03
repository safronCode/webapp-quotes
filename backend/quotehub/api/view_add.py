import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quotehub.models import QuoteView


@csrf_exempt
@login_required
def view_add (request):
    quote_id = int(json.loads(request.body).get('quote_id'))
    if QuoteView.objects.filter(quote_id=quote_id, user=request.user).exists():
        return JsonResponse({"ok": False})

    QuoteView.objects.create(quote_id=quote_id, user=request.user)
    return JsonResponse({"ok": True})
