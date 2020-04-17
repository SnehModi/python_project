from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^Register$', views.signup_view, name='register'),

    url(r'^Login$', views.login_view, name='login'),

    url(r'^Logout$', views.logout_view, name='logout'),

    url(r'^Donate$', views.donate_view, name='donate'),

    url(r'^Donate2$', views.donate2_view, name='donate2'),

    url(r'^Donate3$', views.donate3_view, name='donate3'),

    url(r'^Donate4$', views.donate4_view, name='donate4'),

    url(r'^Donate1$', views.donate1_view, name='donate1'),

    url(r'^Home$', views.home_view, name='home'),

    url(r'^About$', views.about_view, name='about'),

    url(r'^Earthquake$', views.earth_view, name='earthquake'),

    url(r'^Flood$', views.flood_view, name='flood'),

    url(r'^Drought$', views.drth_view, name='drought'),

    url(r'^Landslide$', views.land_view, name='landslide'),

    url(r'^ThankYou$', views.thankyou_view, name='thankyou'),
]
