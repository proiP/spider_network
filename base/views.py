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
    context = {} # python dictionary to be sent to the template
    
    nm = nmap.PortScanner() 
    host_ip_address =  get_ip_address('wlp3s0') # current host ip addess. wlp should change depending on os 
    
    context['host_ip_address'] = host_ip_address
    
    hosts_data = nm.scan(hosts= host_ip_address + "/24" , arguments="-sP")
    host_list = (host for host in hosts_data['scan'])
    context['host_list'] = host_list
    return render(request, template, context)
    



