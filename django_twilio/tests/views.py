from django.http import HttpResponse

from django_twilio.decorators import twilio_view


@twilio_view
def str_view(request):
	"""A simple test view that returns a string."""
	return '<Response><Sms>Hi!</Sms></Response>'


@twilio_view
def response_view(request):
	"""A simple test view that returns a HttpResponse object."""
	return HttpResponse('<Response><Sms>Hi!</Sms></Response>',
			mimetype='text/xml')
