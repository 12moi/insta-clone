from django.conf.urls import url,include
from . import views


urlpatterns = [
    
    # account/
    url('signup/', views.signup, name='signup'),
    url('account/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url('', views.profile, name='profile'),
    # profile/<username>/
    # user_profile/<username>/
    url('', views.user_profile, name='user_profile'),
    # url('post/<id>', views.post_comment, name='comment'),
    url('search/', views.search_profile, name='search'),
]
