import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from blog.forms import ContactForm
from blog.models import Post
from blog.services.friendlycaptcha import verify_captcha_solution
from mysite.settings import EMAIL_HOST_USER, EMAIL_PORT, EMAIL_HOST_PASSWORD, EMAIL_HOST, FRIENDLY_CAPTCHA_SITE_KEY


def home(request):
    posts = Post.published.all()
    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html', {})


def thanks(request):
    return render(request, 'thanks.html', {})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'post_detail.html', {'post': post})


def experience(request):
    return render(request, 'experience.html', {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            captcha_solution = request.POST.get('frc-captcha-solution', '')
            if not verify_captcha_solution(captcha_solution):
                return render(request, 'invalid_form_verification.html')
            msg = MIMEMultipart()
            msg['From'] = EMAIL_HOST_USER
            msg['To'] = EMAIL_HOST_USER
            msg['Subject'] = f'Personal site: {form_data["subject"]}'
            message = f'Name: {form_data["name"]}\n' \
                      f'Email address: {form_data["email_address"]}\n\n' \
                      f'{form_data["message"]}'
            msg.attach(MIMEText(message))
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.ehlo()
                server.starttls()
                server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                server.sendmail(EMAIL_HOST_USER, EMAIL_HOST_USER, msg.as_string())
            return HttpResponseRedirect('/thanks')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'captcha_site_key': FRIENDLY_CAPTCHA_SITE_KEY})
