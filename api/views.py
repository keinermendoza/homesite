from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .forms import ContactEmail

def email_contact(request):
    if request.method == 'POST':
        form = ContactEmail(request.POST)
        if form.is_valid():
            # send email to me with the content and sender
            # send authomatic message to the user
            return JsonResponse({'message':'Email Suceffully Sended, Check out your email inbox'}, status=200)
        else:
            return JsonResponse({'error':"Please check if there is a misstype in the email field. It's not a valid email."}, status=400)
        
    return JsonResponse(status=405)
