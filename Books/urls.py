from django.conf.urls import url
from . import views



urlpatterns=[
     url(r'^book/$',views.ListBookDetails.as_view(),name='book_list'),
     
     url(r'^book/(?P<slug>[-\w]+)$',views.ViewBookDetails.as_view(),name='book_detail'),
     
     url(r'^book/(?P<slug>[-\w]+)/delete/$',views.DeleteBookDetails.as_view(),name='book_delete'),
     
     url(r'^book/create/$',views.CreateBookDetails.as_view(),name='book_create'),
     
    url(r'^book/update/(?P<slug>[-\w]+)/$',views.UpdateBookDetails.as_view(),name='book_update'),
    ]