from django.conf.urls import url,include
from . import views


urlpatterns = [
    # url('signup/', views.signup, name='signup'),
    # url('account/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    
]
