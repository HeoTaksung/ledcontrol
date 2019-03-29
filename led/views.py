from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO

# Create your views here.
LED_RED = 16
LED_GREEN = 20
LED_BLUE = 21

GPIO.setmode(GPIO.BCM)

def blinker(request):
	if 'redon' in request.POST:
		GPIO.setup(16, GPIO.OUT)
		GPIO.output(LED_RED,True)
		#return HttpResponse('RED ON!')
		
	elif 'redoff' in request.POST:
		GPIO.setup(16, GPIO.OUT)
		GPIO.output(LED_RED,False)
		#return HttpResponse('RED OFF!')
		
	elif 'greenon' in request.POST:
		GPIO.setup(20, GPIO.OUT)
		GPIO.output(LED_GREEN,True)
		#return HttpResponse('GREEN ON!')
		
	elif 'greenoff' in request.POST:
		GPIO.setup(20, GPIO.OUT)
		GPIO.output(LED_GREEN,False)
		#return HttpResponse('GREEN OFF!')
		
	elif 'blueon' in request.POST:
		GPIO.setup(21, GPIO.OUT)
		GPIO.output(LED_BLUE,True)
		#return HttpResponse('BLUE ON!')
		
	elif 'blueoff' in request.POST:
		GPIO.setup(21, GPIO.OUT)
		GPIO.output(LED_BLUE,False)
		#return HttpResponse('BLUE OFF!')
		
	return render(request, 'control.html')



"""

def redon(request):
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(LED_RED,True)
	return HttpResponse('')
	
def redoff(request):
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(LED_RED,False)
	return HttpResponse('')
	
def greenon(request):
	GPIO.setup(20, GPIO.OUT)
	GPIO.output(LED_GREEN,True)
	return HttpResponse('')
	
def greenoff(request):
	GPIO.setup(20, GPIO.OUT)
	GPIO.output(LED_GREEN,False)
	return HttpResponse('')
	
def blueon(request):
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(LED_BLUE,True)
	return HttpResponse('')
	
def blueoff(request):
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(LED_BLUE,False)
	return HttpResponse('')
"""
