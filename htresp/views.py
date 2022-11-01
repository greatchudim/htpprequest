from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def home_view(payload):
    payload = {"slackUsername": "greatchudim", "backend": True, "age": 29,
               "bio": "An Enthusiast Python Programmer looking at making more waves and growing better"}

    r = requests.get("https://httpbin.org/get", params=payload)
    return HttpResponse(r.url)
