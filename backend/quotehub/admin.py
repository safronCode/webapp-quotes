from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'source', 'weight')

    def short_text(self, obj):
        return obj.text[:50]+'\t...'

    short_text.short_description = 'Text'

admin.site.register(Quote, QuoteAdmin)
