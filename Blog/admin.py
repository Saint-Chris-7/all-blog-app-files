from django.contrib import admin
from .models import Articles,Authors,Readers
#Register your models here.

admin.site.register(Authors)
admin.site.register(Readers)
admin.site.register(Articles)

