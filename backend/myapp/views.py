from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse

# Create your views here.
def index(request):
    return JsonResponse(
        {'message':"You Have Done It!"}, status=200
    )