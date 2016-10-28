from django.contrib import admin
from main.models import Keja


# Register your models here.

class KejaAdmin(admin.ModelAdmin):
	keja=Keja.objects.filter()
	list_display = ('rentals_name','town','locality','pk','_submission_time',)
	list_filter = ['_submission_time']
	search_fields = ['town']

admin.site.register(Keja, KejaAdmin)
