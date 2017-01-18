from django.contrib import admin

# Register your models here.
from mirror.models import season, seriesRus, seriesEng, subscribers

admin.site.register(season)
admin.site.register(seriesRus)
admin.site.register(seriesEng)
admin.site.register(subscribers)
