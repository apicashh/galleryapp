from django.shortcuts import render
from django.views.generic.list import ListView
from .models import GalleryIsland, BestSite, GallerySMC, Photosession, Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class GalleryPagView(ListView):

    def get(self, request):
        dump_list = GalleryIsland.objects.all().order_by('-id')
        paginator = Paginator(dump_list, 60)  # Show 60 contacts per page
        page = request.GET.get('page')
        list = GallerySMC.objects.all()[:6]
        list_photosession = Photosession.objects.all().order_by('-id')[:12]

        try:
            # Если существует, то выбираем эту страницу
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # Если None, то выбираем первую страницу
            queryset = paginator.page(1)
        except EmptyPage:
            # Если вышли за последнюю страницу, то возвращаем последнюю
            queryset = paginator.page(paginator.num_pages)
        context = {
            "object_list": queryset,
            "title": "List",
            "list": list,
            "list_photosession": list_photosession,

        }
        return render(request, 'GalleryIndex.html', context)


class BestSiteView(ListView):

    def get(self, request):
        dump_list = GalleryIsland.objects.all().order_by('?')[:24]
        sites_list = BestSite.objects.all().order_by('date_added')
        context = { "sites_list": sites_list, "dump_list": dump_list}
        return render(request, 'BestSites.html', context)


class PhotosView(ListView):

    def get(self, request, photosession_id):
        dump_list = GalleryIsland.objects.all().order_by('?')[:24]
        photosession = Photosession.objects.get(id=photosession_id)
        photos = photosession.photo_set.all()
        context = { "photosession": photosession, "photos": photos, "dump_list": dump_list}
        return render(request, 'Photos.html', context)


class GalleryView(ListView):
    def get(self, request):
        dump_list = GalleryIsland.objects.all().order_by('-id')
        paginator = Paginator(dump_list, 120)  # Show 60 contacts per page
        page = request.GET.get('page')
        list = GallerySMC.objects.all()[:6]

        try:
            # Если существует, то выбираем эту страницу
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # Если None, то выбираем первую страницу
            queryset = paginator.page(1)
        except EmptyPage:
            # Если вышли за последнюю страницу, то возвращаем последнюю
            queryset = paginator.page(paginator.num_pages)
        context = {
            "object_list": queryset,
            "title": "List",
            "list": list,
        }
        return render(request, 'bar/Gallery.html', context)


class PhotoGalleryView(ListView):

    def get(self, request):
        list = GallerySMC.objects.all()[:12]
        list_photosession = Photosession.objects.all().order_by('-id')
        context = {
            "list": list,
            "list_photosession": list_photosession,
        }
        return render(request, 'bar/Photogallery.html', context)


class ModelGalleryView(ListView):

    def get(self, request):
        list = GallerySMC.objects.all()[:90]
        dump_list = GalleryIsland.objects.all().order_by('?')[:12]
        context = {
            "list": list,
            "dump_list": dump_list,
        }
        return render(request, 'bar/Modelgallery.html', context)