from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView
from .models import Voyage, EvenementSportif, Reservation


from django.urls import reverse_lazy
from .forms import ReservationForm, VoyageForm, EvenementSportifForm


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Réserve les opérations de gestion aux superutilisateurs."""

    def test_func(self):
        return self.request.user.is_superuser


class AccueilView(TemplateView):
    template_name = 'accueil.html'


class VoyageDetailView(DetailView):
    model = Voyage
    template_name = 'voyage_detail.html'
    context_object_name = 'voyage'

class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_form.html'
    success_url = reverse_lazy('reservations_lists')

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

class ReservationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_form.html'
    success_url = reverse_lazy('reservations_lists')

    def test_func(self):
        return self.get_object().client == self.request.user

class UserReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservations_lists.html'

    def get_queryset(self):
        return Reservation.objects.filter(client=self.request.user)
    
class ReservationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reservation
    template_name = 'reservation_confirm_delete.html'  # utile si tu ne veux pas que la suppression passe par modale
    success_url = reverse_lazy('reservations_lists')

    def test_func(self):
        return self.get_object().client == self.request.user

class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'
    context_object_name = 'reservation'

    def get_queryset(self):
        return Reservation.objects.filter(client=self.request.user)
    
class ReservationListViewAdmin(AdminRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservation_list_admin.html'
    context_object_name = 'reservations'

# REGISTRATIONS    
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


# VOYAGES
class VoyageListView(ListView):
    model = Voyage
    template_name = 'voyage_list.html'
    context_object_name = 'voyages'

class VoyageCreateView(AdminRequiredMixin, CreateView):
    model = Voyage
    form_class = VoyageForm
    template_name = 'voyage_form.html'
    success_url = reverse_lazy('voyage_list')

class VoyageUpdateView(AdminRequiredMixin, UpdateView):
    model = Voyage
    form_class = VoyageForm
    template_name = 'voyage_form.html'
    success_url = reverse_lazy('voyage_list')
    
class VoyageDeleteView(AdminRequiredMixin, DeleteView):
    model = Voyage
    template_name = 'voyage_confirm_delete.html'  
    success_url = reverse_lazy('voyage_list')

# EVENEMENTS
class EvenementListView(ListView):
    model = EvenementSportif
    template_name = 'evenement_list.html'
    context_object_name = 'evenements'

    def get_queryset(self):
        queryset = EvenementSportif.objects.all()
        voyage_id = self.request.GET.get('voyage')
        if voyage_id:
            queryset = queryset.filter(voyages__id=voyage_id)  
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voyages'] = Voyage.objects.all()
        context['voyage_actif'] = self.request.GET.get('voyage')
        return context


class EvenementCreateView(AdminRequiredMixin, CreateView):
    model = EvenementSportif
    form_class = EvenementSportifForm
    template_name = 'evenement_form.html'
    success_url = reverse_lazy('evenement_list')

class EvenementUpdateView(AdminRequiredMixin, UpdateView):
    model = EvenementSportif
    form_class = EvenementSportifForm
    template_name = 'evenement_form.html'
    success_url = reverse_lazy('evenement_list')

class EvenementDetailView(LoginRequiredMixin, DetailView):
    model = EvenementSportif
    template_name = 'evenement_detail.html'
    context_object_name = 'evenement'

class EvenementDeleteView(AdminRequiredMixin, DeleteView):
    model = EvenementSportif
    template_name = 'evenement_confirm_delete.html'
    success_url = reverse_lazy('evenement_list')
