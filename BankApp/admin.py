from django.contrib import admin

# Register your models here.

from .models import Banks, Blood, RequesterModel , DonnerModel ,RequestedBlood
 
@admin.register(Banks)
class RequestDemoAdmin(admin.ModelAdmin):
  List_display = [field.name for field in
Banks._meta.get_fields()]