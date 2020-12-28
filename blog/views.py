from django.core.mail import send_mail
from django.shortcuts import render

from blog.forms import EmailForm
from mysite.settings import EMAIL_HOST_USER


def home(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            send_mail(f'Personal site: {form_data["subject"]}',
                      f'From {form_data["from_email"]}:\n{form_data["message"]}',
                      form_data['from_email'],
                      [EMAIL_HOST_USER])
    else:
        form = EmailForm()

    return render(request, 'contact.html', {'form': form})
