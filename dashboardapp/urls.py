from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.home,name = 'home'),
    url(r'^new/post', views.new_post, name='new-post'),
    url(r'^post/(\d+)', views.post, name='post'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    url(r'^profile/(\d+)$',views.profile,name = 'profile'),
    url(r'^like/(\d+)/$',views.likes, name = 'like'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)