from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.urls.base import reverse
# Create your models here.
class Book(models.Model):
    added_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,related_name='book_add',on_delete=models.CASCADE)
    last_edited_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,related_name="book_edit",on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    title=models.CharField(max_length=20)
    description=models.TextField();
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    
    def __Unicode__(self):
        return self.title
    
    def getBookUrl(self):
        
        return reverse('book_detail',kwargs={'slug':self.slug})
    def getBooksUrl(self):
        return reverse('book_list')
    def deleteBookUrl(self):
        return reverse('book_delete',kwargs={'slug':self.slug})
    
    def updateBookUrl(self):
        return reverse('book_update',kwargs={'slug':self.slug})
    
    
    
      
def pre_save_book(sender,instance,**kwargs):
    slug=slugify(instance.title)
    instance.slug=slug
    

pre_save.connect(pre_save_book, sender=Book)
    