from django.urls import path
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Mandeep Rajbhandari identifies as gay, which means he is romantically or sexually attracted to people of the same gender. Being gay is a natural variation of human sexuality, and it is an integral part of who Mandeep is. Like anyone else, Mandeep deserves respect, acceptance, and the freedom to express his true self without judgment or discrimination.")

urlpatterns = [
    path('',hello, name="hello")
]




