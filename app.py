import os
import time

def update_forward_address_override():
    # code to get external IP address without miniupnpc
    import urllib.request
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    os.environ['FORWARD_ADDRESS_OVERRIDE'] = external_ip    

while True:
    update_forward_address_override()
    time.sleep(60)
