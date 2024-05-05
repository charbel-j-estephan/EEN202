# contact/views.py
from django.http import JsonResponse

from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage
from .forms import ContactForm
import os
from django.core.mail import send_mail


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Create the email content as plain text
            email_content = f"From: {name}\nEmail: {email}\n{message}"

            # Send the email
            send_mail(
                subject="Contact Form Submission from {}".format(name),
                message=email_content,
                from_email="charbelstephan13@gmail.com",
                recipient_list=["charbelstephan13@gmail.com"],
            )

            return redirect("success")
    else:
        form = ContactForm()
    return render(request, "products/products_list.html", {"form": form})


def success_view(request):
    # You can customize the success message as needed
    success_message = "Your message has been sent successfully!"
    return JsonResponse({"success": True, "message": success_message})
