from django.conf.urls import url
from . import views
from app1.views import CbvView

urlpatterns = [
    url(r'^fbv/',views.fbv,name='fbv'),
    url(r'^cbv/',CbvView.as_view())
]