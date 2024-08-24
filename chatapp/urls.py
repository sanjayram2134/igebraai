from django.urls import path
from . import views
# from .views import chat_view

urlpatterns = [
    path('', views.home, name='home'),  # Route for the home page
    #path('chat/', chat_view, name='chat'),  # Route for the chat history page
]
