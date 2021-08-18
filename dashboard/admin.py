from django.contrib import admin
from .models import CarEvaluation

@admin.register(CarEvaluation)
class itemAdmin(admin.ModelAdmin):
    list_display = ('buying','maint', 'doors', 'persons', 'lug_boot', 'safety', 'predictions')
    

