"""bysj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from index import views as index_views
from importfile import views as importfile_views
from exportfile import views as exportfile_views
from datatable import views as datatable_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/', include('users.urls')),
    url(r'^register/', index_views.register, name='register'),
    url(r'^login/', index_views.login, name='login'),
    url(r'^home/', index_views.index, name='index'),
    url(r'^import/', importfile_views.importfile, name='importfile'),
    url(r'^export/', exportfile_views.exportfile, name='exportfile'),
    url(r'^datatable/', datatable_views.table, name='datatable'),
    #url(r'^test1/',datatable_views.test1, name='test1' ),
    #url(r'^test2/', datatable_views.test2,name='test2')

] #+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
