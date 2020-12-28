from django.core.mail import send_mail
from django.shortcuts import render

from blog.forms import EmailForm
from blog.models import Post
from mysite.settings import EMAIL_HOST_USER


def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html', {})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})


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
