from django.contrib import admin
from galleryapp.models import GalleryIsland, BestSite, GallerySMC, Photosession, Photo

class ImageInline(admin.StackedInline):
    model = Photo

@admin.register(Photosession)
class PhotosessionAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]

admin.site.register(GalleryIsland)
admin.site.register(GallerySMC)
admin.site.register(BestSite)
#admin.site.register(Photosession)
admin.site.register(Photo)





