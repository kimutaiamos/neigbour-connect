from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home,name ='home'),
    url(r'^home', views.home,name ='home'),
    url(r'^Signup',views.signup, name='signup'),
    url(r'^index', views.index, name = 'index'),
    url(r'^Nairobi', views.Nairobi, name = 'Nairobi'),
    url(r'^london', views.london, name = 'london'),
    url(r'user/(?P<username>\w+)', views.profile,name='profile'),
    url(r'^upload/$', views.upload_post, name='upload_post'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^post/(?P<post_id>\d+)', views.single_post, name='single_post'),
    url(r'^search/', views.search, name='search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
