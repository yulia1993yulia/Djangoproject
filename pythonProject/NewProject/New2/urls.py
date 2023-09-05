from django.contrib import admin
# from New2.views import test, get_profession, view_humans, add_human, test2
from django.urls import path
from New2.views import HomeHumans, HumansByProfession, ViewHumans, AddHumans, register, user_login, user_logout
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', test, name='Home2'),
    # path('profession/<int:profession_id>', get_profession, name='Profession'),
    # path('human/<int:human_id>', view_humans, name='View_humans'),
    # path('human/add_human', add_human, name='Add_human'),
    # path('test2/', test2, name='Test2'),
    path('', HomeHumans.as_view(), name='Home2'),
    path('profession/<int:profession_id>', HumansByProfession.as_view(), name='Profession'),
    path('Human/<int:pk>', ViewHumans.as_view(), name='View_humans'),
    path('human/add_human', AddHumans.as_view(), name='Add_human'),
    path('register/', register, name='Register'),
    path('login/', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
]



