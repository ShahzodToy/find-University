from django.contrib import admin
from university import models


admin.site.index_title = 'University finder'
admin.site.site_header = 'University Admin'
admin.site.site_title = 'University top'



class ContactInfoInline(admin.TabularInline):
    model = models.SocialMedia
    extra = 1 

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('title','univer_type','contract_sum_range')
    inlines = [ContactInfoInline]


admin.site.register(models.ContactInfo)
admin.site.register(models.ContactInfoDetail)
admin.site.register(models.SocialMedia)
admin.site.register(models.UniversityFaculty)
admin.site.register(models.EducationLanguage)
admin.site.register(models.UniversityDirections)
admin.site.register(models.PriceFaculty)

