from django.contrib import admin
from main.models import Keja


# Register your models here.

class KejaAdmin(admin.ModelAdmin):
	keja=Keja.objects.filter()
	list_display = ('rentals_name','town','locality','pk','pub_date',)
	list_filter = ['pub_date']
	search_fields = ['town']

admin.site.register(Keja, KejaAdmin)
