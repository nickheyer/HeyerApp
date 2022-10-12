from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import RedirectView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as UserModel
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver


from . import forms
from . import models

class Home(TemplateView):
    template_name = "heyercode/index.html"
