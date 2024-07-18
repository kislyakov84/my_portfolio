from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Author, Message, Category


def index(request):
    categories = Category.objects.all()

    return render(request, "index.html")


def about(request):
    author = Author.objects.get()
    return render(request, "about.html", {'author': author})


def contact(request):
    if request.method == 'POST':
        msg = Message(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        msg.save()
        messages.success(request, 'Сообщение отправлено!')
        return redirect('contact')

    return render(request, 'contact.html')
