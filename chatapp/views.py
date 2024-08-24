from django.shortcuts import render, redirect
from .mistral import generate_response_mistral
from .llama import generate_response_llama
from .mongo import insert_data
from django.http import JsonResponse
from pymongo import MongoClient
import os
import uuid

# MongoDB setup
uri = "mongodb+srv://sanjayram2134:ram_2134@cluster0.1mxxz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['mydb1']

def home(request):
    # Check if a new session is requested
    if 'new_session' in request.GET:
        session_id = str(uuid.uuid4())
        response = redirect('home')
        response.set_cookie('session_id', session_id)
        return response

    # Get the current session ID from the query parameters or cookies
    session_id = request.GET.get('session_id') or request.COOKIES.get('session_id')
    
    if not session_id:
        session_id = str(uuid.uuid4())
        response = redirect('home')
        response.set_cookie('session_id', session_id)
        return response

    if request.method == 'POST':
        model_choice = int(request.POST.get('model_choice'))
        query = request.POST.get('query')

        if model_choice == 1:
            ans = generate_response_mistral(query)
        elif model_choice == 2:
            ans = generate_response_llama(query)

        # Use session_id to insert data into the correct collection
        collection = db[session_id]
        document = {"query": query, "response": ans}
        collection.insert_one(document)

        return render(request, 'chatapp/home.html', {'query': query, 'ans': ans, 'session_id': session_id})

    # Fetch chat history for the current session
    collection = db[session_id]
    chat_history = list(collection.find())

    # Fetch all session IDs
    session_ids = db.list_collection_names()

    return render(request, 'chatapp/home.html', {
        'chat_history': chat_history, 
        'session_id': session_id, 
        'session_ids': session_ids
    })
