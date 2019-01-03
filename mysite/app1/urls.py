from django.conf.urls import url
from . import views
from app1.views import CbvView,DogView

urlpatterns = [
    url(r'^fbv/',views.fbv,name='fbv'),
    url(r'^cbv/',CbvView.as_view()),
    url(r'^dog/',DogView.as_view()),
]