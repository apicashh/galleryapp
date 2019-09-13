from django.db import models
import uuid
#from uuid import uuid4



class GalleryIsland(models.Model):
    name = models.CharField(max_length=300)
    url = models.URLField()
    thumb = models.URLField()
    description = models.CharField(max_length=300)
    thumbnail200 = models.URLField()
    direct_url = models.URLField()
    date_added = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GallerySMC(models.Model):
    name = models.CharField(max_length=300)
    url = models.URLField()
    thumb = models.FileField(upload_to='media/pic')
    direct_url = models.URLField()
    site_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BestSite(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/best_sites_img')
    content = models.TextField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.text



class Photosession(models.Model):
    title = models.CharField(max_length=50)
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    text = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='media/Photosession')

    def __str__(self):
        return self.title

def get_member_upload_to(instance, filename):
    new_filename = '{}.{}'.format(uuid.uuid4, filename.split('.')[-1])
    return "media/Photosessions/{}/{}".format(instance.owner.id, new_filename)

class Photo(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(Photosession, on_delete=models.CASCADE)
    date_taken = models.DateField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to=get_member_upload_to, blank=True, null=True)

    def __str__(self):
        return self.title