from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Save the form data to the database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Send an email
        send_mail(
            subject=f"New Contact Form Submission: {subject}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # Add a success message and redirect
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')  # Redirect to a thank you page or the contact form page
    return render(request, 'hia_app_templates/index.html')

def about_view(request):
    return render(request, 'hia_app_templates/about_us.html')

def courses_view(request):
    return render(request, 'hia_app_templates/courses.html')

