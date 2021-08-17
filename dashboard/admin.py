from django.contrib import admin
from .models import CarEvaluation

@admin.register(CarEvaluation)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('buying', 'doors', 'persons', 'lug_boot', 'safety', 'predictions')



