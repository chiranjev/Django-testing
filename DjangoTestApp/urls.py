from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.Home),
    url(r'^create_post/$', views.CreatePost),
    url(r'^view_post/(?P<post_pk>[-\w]+)', views.ViewPost),
    url(r'^get_post/', views.GetPost),
    url(r'^publish_post/', views.PublishPost),
    url(r'home_section/$',views.HomeSection,name='home'),
    url(r'^about_section/$',views.AboutSection,name='about'),
    url(r'^posts/$',views.PostPageView,name='posts'),

]