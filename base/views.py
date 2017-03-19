from django.shortcuts import render

import nmap # nework mapper
import socket 
import fcntl
import struct


# Create your views here.

# This function gets the ip address without using external python package
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def home_view(request):
    template = 'body/home.html'
    print 'test'
    context = {} # python dictionary to be sent to the template
    
    nm = nmap.PortScanner() 
    host_ip_address =  get_ip_address('wlp3s0') # current host ip addess. wlp should change depending on os 
    
    context['host_ip_address'] = host_ip_address
    
    return render(request, template, context)
    



