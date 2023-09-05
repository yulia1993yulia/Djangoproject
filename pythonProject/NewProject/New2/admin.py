from django.contrib import admin
from .models import Human, Profession
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class HumanAdminForm(forms.ModelForm):
    Name = forms.CharField(widget=CKEditorUploadingWidget())
    Surname = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Human
        fields = '__all__'


class HumanAdmin(admin.ModelAdmin):
    list_display = ('Name', 'profession', 'Surname', 'Date_of_birth', 'Gender', 'get_photo')
    list_display_links = ('Name', 'Surname')
    search_fields = ('Name', 'Surname')
    list_filter = ('Gender', 'Name')
    list_editable = ['profession']
    fields = ('Name', 'Surname', 'Date_of_birth', 'Photo', 'get_photo', 'profession')
    readonly_fields = ('get_photo', 'Date_of_birth')
    form = HumanAdminForm

    def get_photo(self, obj):
        if obj.Photo:
            return mark_safe(f'<img src="{obj.Photo.url}" width="75">')
        else:
            return 'Фото нет'

    get_photo_description = 'Миниатюра'


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', "title")


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'
