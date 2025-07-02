from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quotehub.models import QuoteLike


@csrf_exempt
@login_required
def like_remove(request):
    quote_id = request.POST.get('quote_id')
    if not QuoteLike.objects.filter(quote=quote_id, user=request.user).exists():
        return JsonResponse({"ok": False})

    QuoteLike.objects.delete(quote=quote_id, user=request.user)
    return JsonResponse({"ok": True})
