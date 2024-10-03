from django.contrib import admin

from .models import Chaivarity,ChaiCertificate,ChaiReview,store


class chaiReviewInline(admin.TabularInline):  # to inject with inline check in chaivarity you see 2 slots of review in line i.e below 
     model=ChaiReview
     extra=2

class ChaivarietyAdmin(admin.ModelAdmin):
     list_display=('name','type','date')      # It will display name and type on db 
     inlines=[chaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
     list_display=('name','location')
     filter_horizontal=('chai_varieties',)


class ChaiCertificateAdmin(admin.ModelAdmin):
     list_display=('chai','certificate_number')


admin.site.register(store,StoreAdmin)
admin.site.register(Chaivarity,ChaivarietyAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
