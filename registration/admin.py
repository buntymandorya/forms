from django.contrib import admin
from .models import demo

# Register your models here.
@admin.register(demo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','states','city','educational','mobile','tools','hours','link','equipment','skills','project','referred','otherLanguage','languages','expertise']



