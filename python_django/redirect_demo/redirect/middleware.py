from django.http import response
from django.middleware.clickjacking import XFrameOptionsMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from django.middleware.common import CommonMiddleware
def redirectMiddeware(getrespone):
    def middeware(self, request):

        return response
    return middeware()