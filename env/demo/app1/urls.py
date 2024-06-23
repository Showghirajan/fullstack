from django.urls import path
from .import views
urlpatterns = [
        path('',views.index,name="index"),
        path('drug/',views.drug,name="drug"),
        path('book/',views.book,name="book"),
        path('doctor/',views.doctor,name="doctor"),
]