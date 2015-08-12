from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.usr_dashboard, name='dashboard'),
    url(r'^login/$', views.do_login, name='login'),
    url(r'^logout/$', views.do_logout, name='logout'),
    url(r'^user/profile/$', views.usr_profile, name='profile'),
    url(r'^user/admin/create/$', views.admin_create, name='create'),
    #url(r'^user/admin/create/create-user/$', views.admin_create_user, name='create-user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
