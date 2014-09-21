"""
register our models for Django's admin
"""

from django.contrib import admin

from .models import Host, Domain, BlacklistedDomain, ServiceUpdater, ServiceUpdaterHostConfig


class DomainAdmin(admin.ModelAdmin):
    list_display = ("name", "public", "available", "created_by")
    list_filter = ("created", "public", "available")


class HostAdmin(admin.ModelAdmin):
    list_display = ("name", "domain", "created_by", "client_faults", "abuse", "abuse_blocked")
    list_filter = ("created", "abuse", "abuse_blocked", "domain")


class BlacklistedDomainAdmin(admin.ModelAdmin):
    list_display = ("name_re", "created_by")
    list_filter = ("created", )


admin.site.register(BlacklistedDomain, BlacklistedDomainAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(ServiceUpdater)
admin.site.register(ServiceUpdaterHostConfig)
