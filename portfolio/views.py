from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Author, Message, Category, Work, Testimony


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


def work_detail(request, slug):
    work = get_object_or_404(Work, slug=slug)
    testimonies = Testimony.objects.all()
    context = {
        'work': work,
        'testimonies': testimonies,
    }

    return  render(request, 'work_detail.html', context)