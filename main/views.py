from django.shortcuts import render
from django.core.mail import EmailMessage
def home(request): return render(request, 'home.html')
def about(request): return render(request, 'about.html') 
def services(request): return render(request, 'services.html')
def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email_msg = EmailMessage(
            f'New message from {name}',
            f'From: {name} ({email})\n\n{message}',
            'noreply@phillashcool.com',
            ['kyliekezaih@gmail.com'],
            reply_to=[email],
        )
        email_msg.send()
        success = True
    return render(request, 'contact.html', {'success': success})
# Create your views here.
