from django.shortcuts import render, get_object_or_404, redirect
from .models import Human, Profession
from .forms import HumansForm, UserRegisterForm, UserLoginForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registration is success')
            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Error registration')
    else:
        form = UserRegisterForm()
    return render(request, 'New2/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home2')
    else:
        form = UserLoginForm()
    return render(request, 'New2/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('Login')


class HomeHumans(ListView):
    model = Human
    context_object_name = 'humans'
    template_name = 'New2/home_humans_list.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    # def get_queryset(self):
    #      return Human.objects.filter(Photo=False)


class HumansByProfession(ListView):
    model = Human
    context_object_name = 'humans'
    template_name = 'New2/home_humans_list.html'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Profession.objects.get(pk=self.kwargs['profession_id'])
        return context

    def get_queryset(self):
        return Human.objects.filter(profession_id=self.kwargs['profession_id']).select_related('profession')


class ViewHumans(DetailView):
    model = Human
    context_object_name = 'humans_item'
    template_name = 'New2/view_humans.html'


class AddHumans(CreateView):
    form_class = HumansForm
    template_name = 'New2/add_human.html'
    login_url = '/admin/'

# def test(request):
#     objects = ['Join', 'Pall', 'Roi', 'Join2', 'Pall2', 'Roi2']
#     paginator = Paginator(object, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     return render(request, 'New2/test2.html', {'page_obj':page_objects})

# def add_human(request):
#     if request.method == 'POST':
#         form = HumansForm(request.POST)
#         if form.is_valid:
#             # humans = Human.objects.create(**form.cleaned_data)
#             humans = form.save()
#             return redirect(humans)
#     else:
#         form = HumansForm()
#     return render(request, 'New2/add_human.html', {'form': form})

# def view_humans(request, human_id):
#     humans_item = get_object_or_404(Human, pk=human_id)
#     context = {'humans_item': humans_item}
#     return render(request, 'New2/view_humans.html', context=context)

# def get_profession(request, profession_id):
#     humans = Human.objects.filter(profession_id=profession_id)
#     profession = Profession.objects.get(pk=profession_id)
#     context = {
#         'humans': humans,
#         'profession': profession
#     }
#     return render(request, 'New2/profession.html', context=context)
