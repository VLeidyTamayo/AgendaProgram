from django.urls import path

from contactos import views 


urlpatterns = [
    path('',views.ContactListView.as_view(), name='contactos_list'),
    path('new/',views.ContactCreateView.as_view(), name='contactos_new'),
    path('<int:pk>/edit/',views.ContactUpdateView.as_view(), name='contactos_edit'),
    path('<int:pk>/delete/',views.ContactDeleteView.as_view(), name='contactos_delete'),

]
