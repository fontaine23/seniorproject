from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def highlights(request):
	return render(request, 'highlights.html', {})

def gallery(request):
	return render(request, 'gallery.html', {})

def contact(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']

		# send an email
		send_mail(
			name,
			message,
			email,
			['fontainet023@gmail.com'],
			)
		return render(request, 'contact.html', {'name': name})	

	else:	
		return render(request, 'contact.html', {})			