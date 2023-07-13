from django.shortcuts import render
from django.core.mail import send_mail

# def email(request):
#     send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )
#     return render(request, "app/email.html")

def email(request):
     return render(request, 'app/email.html', {})