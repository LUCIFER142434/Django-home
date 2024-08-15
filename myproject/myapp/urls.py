from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about,name ='about'),
    path('blog/',views.blog,name ='blog'),
    path('class/',views.clas,name ='class'),
    path('',views.copy_blog_fun,name="index"),
    # path('mark',views.copy_li_fun,name="mark")
]