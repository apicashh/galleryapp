from django.urls import path
from . import views
from galleryapp.views import GalleryPagView, BestSiteView, PhotosView, GalleryView, PhotoGalleryView, ModelGalleryView


urlpatterns = [
	path('', GalleryPagView.as_view(), name="index"),
	path('Best_sites', BestSiteView.as_view(), name='Best_sites'),
	path('Photos/<photosession_id>', PhotosView.as_view(), name='Photos'),
	path('Gallery', GalleryView.as_view(), name='Gallery'),
	path('Photogallery', PhotoGalleryView.as_view(), name='Photogallery'),
	path('Modelgallery', ModelGalleryView.as_view(), name='Modelgallery')
	#path('photo/<photosession_id>', views.photo, name='Photos'),
]
