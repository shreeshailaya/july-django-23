from django.contrib import admin
from models_relations.models import Album, Song

# Register your models here.
@admin.register(Album)
class AlbumContent(admin.ModelAdmin):
    pass

admin.site.register(Song)
    

