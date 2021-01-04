from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse
from .forms import ContactForm


def contact(request):
    """
    A view to return contact page and render the form
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    # to capture the user email it's displayd in subject field and can be responded to
                    f"Message from {name}, <{email}>", 
                    message,
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                
                return redirect('contact')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)