from django.contrib import admin
from models_relations.models import Album, Song, Book, Author, Car, Vehicle

# Register your models here.
@admin.register(Album)
class AlbumContent(admin.ModelAdmin):
    pass

admin.site.register(Song)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Car)
admin.site.register(Vehicle)

