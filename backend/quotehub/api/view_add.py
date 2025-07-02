from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quotehub.models import QuoteView


@csrf_exempt
@login_required
def view_add (request):
    quote_id = request.POST.get('quote_id')
    if not QuoteView.objects.filter(quote=quote_id, user=request.user).exists():
        return JsonResponse({"ok": False})

    QuoteView.objects.create(quote=quote_id, user=request.user)
    return JsonResponse({"ok": True})
