from django.shortcuts import render, HttpResponseRedirect, redirect
from home.models import Settings, ContactMessage, ContactForm, Cuorses
import requests
from django.contrib import messages

TELEGRAM_BOT_TOKEN = '7851922547:AAGySHzjYPWnvmJAEOv49cY-WMOwp1X4JH4'
TELEGRAM_CHANNEL = '@zayavka_uz'
TELEGRAM_API = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'


def index(request):
    courses = Cuorses.objects.all().order_by('id')[:4]
    context = {
        'courses': courses
    }
    return render(request, 'home.html', context)

def about(request):

    return render(request, 'about.html')

def course(request):
    courses = Cuorses.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']
            message_text = f'🌐 New message: \n \nName: {name} \nPhone: {phone} \nSubject: {subject} \nMessage: {message}'
            telegram_api_url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
            telegram_params = {'chat_id': TELEGRAM_CHANNEL, 'text': message_text}
            requests.post(telegram_api_url, params=telegram_params)
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Thanks, " + data.name + ". We received your message and will respond shortly.")
            return redirect('/contact')
    setting = Settings.objects.get()
    form = ContactForm()
    context = {'setting': setting, 'form': form}
    return render(request, 'contacts.html', context)
