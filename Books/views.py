from django.shortcuts import render
from django.views.generic import DetailView,ListView,DeleteView,CreateView,UpdateView
from .forms import BookForm
# Create your views here.
from .models import Book
from django.urls.base import reverse

class ViewBookDetails(DetailView):
    model =Book
    


class ListBookDetails(ListView):
    model =Book
    


class DeleteBookDetails(DeleteView):
    model =Book
    
    def get_success_url(self):
        
        return reverse('book_list')
    
#get_absolute_url
class CreateBookDetails(CreateView):
    model =Book
    form=BookForm
    fields =['title','description']
    
    def get_success_url(self):
        
        return reverse('book_list')
    
  

class UpdateBookDetails(UpdateView):
    model =Book
    form=BookForm
    fields =['title','description']
    
    def get_context_data(self, **kwargs):
        context=super(UpdateBookDetails,self).get_context_data()
      
        context['view_type']='update'
        
        return context
    
    def get_success_url(self):
        
        return reverse('book_list')
    
  
    