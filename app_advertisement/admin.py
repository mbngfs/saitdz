from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auct', 'get_image']
    list_filter = ['auct', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    search_fields = ['title', 'id', 'price']

    @admin.action(description='Disable auction')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auct=False)

    @admin.action(description='Enable auction')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auct=True)


admin.site.register(Advertisement, AdvertisementAdmin)
