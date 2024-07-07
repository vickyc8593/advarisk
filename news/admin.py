# myapp/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import SearchResult  # Assuming your SearchResult model is here

# Register your SearchResult model
@admin.register(SearchResult)
class SearchResultAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'title', 'published_at', 'created_at')
    list_filter = ('created_at', 'published_at')
    search_fields = ('keyword', 'title')
    ordering = ('-published_at',)


# Custom UserAdmin class
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

    actions = ['block_users', 'unblock_users']

    def block_users(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, _("Selected users have been blocked."))

    block_users.short_description = _("Block selected users")

    def unblock_users(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, _("Selected users have been unblocked."))

    unblock_users.short_description = _("Unblock selected users")


# Unregister the original User model and register the custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
