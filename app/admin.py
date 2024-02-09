from django.contrib import admin
from .models import *

@admin.register(Baner)
class BanerAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Static)
class StaticAdmin(admin.ModelAdmin):
    list_display = ('count_student',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name',)
    list_display_links = ('id','first_name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Social_acaount)
class Social_acaountAdmin(admin.ModelAdmin):
    list_display = ('order',)