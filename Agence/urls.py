from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

class LogoutViewGET(LogoutView):
    http_method_names = ['get', 'post']

urlpatterns = [
    path('', views.AccueilView.as_view(), name='accueil'),
    # RESERVATIONS
    path('reservations/create/', views.ReservationCreateView.as_view(), name='reservation_create'),
    path('mes-reservations/', views.UserReservationListView.as_view(), name='reservations_lists'),
    path('reservations/admin/', views.ReservationListViewAdmin.as_view(), name='reservation_admin_list'),
    path('reservations/detail/<int:pk>/', views.ReservationDetailView.as_view(), name='reservation_detail'),
    path('reservations/modifier/<int:pk>/', views.ReservationUpdateView.as_view(), name='reservation_modifier'),
    path('reservations/supprimer/<int:pk>/', views.ReservationDeleteView.as_view(), name='reservation_supprimer'),
    
    # REGISTRATIONS
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/',LogoutViewGET.as_view(template_name='registration/logout.html'), name='logout'),
    
    # VOYAGES
    path('voyage/<int:pk>/', views.VoyageDetailView.as_view(), name='voyage_detail'),
    path('voyages/', views.VoyageListView.as_view(), name='voyage_list'),
    path('voyages/ajouter/', views.VoyageCreateView.as_view(), name='voyage_ajouter'),
    path('voyages/modifier/<int:pk>/', views.VoyageUpdateView.as_view(), name='voyage_modifier'),
    path('voyages/supprimer/<int:pk>/', views.VoyageDeleteView.as_view(), name='voyage_supprimer'),

    # EVENEMENTS SPORTIFS
    path('evenements/', views.EvenementListView.as_view(), name='evenement_list'),
    path('evenements/ajouter/', views.EvenementCreateView.as_view(), name='evenement_ajouter'),
    path('evenements/modifier/<int:pk>/', views.EvenementUpdateView.as_view(), name='evenement_modifier'),
    path('evenements/detail/<int:pk>/', views.EvenementDetailView.as_view(), name='evenement_detail'),
    path('evenements/supprimer/<int:pk>/', views.EvenementDeleteView.as_view(), name='evenement_supprimer'),
]
