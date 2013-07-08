# Create your views here.
#from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html', 
                              {'errors': errors,
                               'subject': request.POST.get('subject', ''),
                               'message': request.POST.get('message', ''),
                               'email': request.POST.get('email', '')})

def contact_thanks(request):
    return render_to_response('contact_thanks.html')

def send_mail(subject, message, user_email, employee_emails):
    print '''send email "subject = %s, message = %s from user_email = %s  
            TO employee_emails = %s"''' % (subject, message, user_email, employee_emails)
