from django.contrib import admin
from .models import Book
from .forms import BookForm
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=['slug','__Unicode__']
    
    readonly_fields=['updated','timestamp','last_edited_by','added_by']
    
    form=BookForm;
    
    

admin.site.register(Book,BookAdmin);
    
    