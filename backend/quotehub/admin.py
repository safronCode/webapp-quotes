from django.contrib import admin
from .models import Quote, QuoteLike, QuoteDislike, QuoteView


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'source', 'weight')

    def short_text(self, obj):
        return obj.text[:50]+'\t...'

    short_text.short_description = 'Text'


class QuoteLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quote')


class QuoteDislikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quote')


class QuoteViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quote')


admin.site.register(Quote, QuoteAdmin)
admin.site.register(QuoteLike, QuoteLikeAdmin)
admin.site.register(QuoteDislike, QuoteDislikeAdmin)
admin.site.register(QuoteView, QuoteViewAdmin)


