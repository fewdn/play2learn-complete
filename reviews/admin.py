from django.contrib import admin

# Register your models here.
from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['user', 'review', 'created', 'featured']

    #def get_readonly_fields(self, request, obj=None):
    #    if obj:
    #       return ('created')
    #    
    #    return ()