from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.welcome, name="welcome"),
    url('^all/',views.allSweets,name="allSweets"),
    url('^candy/(\d+)',views.candy,name="candy")
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)