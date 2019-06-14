from django.conf.urls import url


from .views import BlogPost_non_createView,BlogPostAPIView,UserLoginAPIView
urlpatterns = [
    url(r'^$', BlogPostAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', BlogPost_non_createView.as_view(), name='post-rud'),
    url(r'^login/',UserLoginAPIView.as_view(),name='log-in'),
]
