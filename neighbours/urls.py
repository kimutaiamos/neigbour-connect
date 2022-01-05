from django.conf.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'^$', views.home,name ='home'),
    path(r'^home', views.home,name ='home'),
    path(r'^signup',views.signup, name='signup'),
    path(r'^index', views.index, name = 'index'),
    path(r'^Nairobi', views.Nairobi, name = 'Nairobi'),
    path(r'^london', views.index, name = 'london'),
    path(r'user/(?P<username>\w+)', views.profile,name='profile'),
    path(r'^upload/$', views.upload_post, name='upload_post'),
    path(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    path(r'^post/(?P<post_id>\d+)', views.single_post, name='single_post'),
    path(r'^search/', views.search, name='search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
