from django.conf.urls import url
from django.contrib import admin
from bcn import views

from django.conf import settings
from django.conf.urls.static import static
# from imageloader import views

urlpatterns = [

    url(r'^$', views.index, name='rootIndex'),
    url(r'^rest/', views.rest, name='rest'),
    url(r'^relax/', views.relax, name='relax'),
    url(r'^living/', views.living, name='living'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^out/', views.out, name='out'),
    url(r'^admin/', admin.site.urls),
    # url(r'^loader/', include('imageloader.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
