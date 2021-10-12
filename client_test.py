import json, time
try:
    import httplib
except:
    import http.client as httplib

http_server = '192.168.0.195:8181'
import json
headers = {'Content-type':'application/json'}
connection = httplib.HTTPConnection(http_server)

class rpi_interface(object):
    def __init__(self):
        #print('you are here gesture')
        pass
        
    def talk(self,vlen):
        foo = {'text':'mode','mode_val':'les','len':vlen}
        json_foo = json.dumps(foo)
        connection.request('POST','/markdown',json_foo,headers)
        response = connection.getresponse()
        print(response.read().decode())
    
        
    def talk1(self,vlen):
        foo = {'text':'talk','angle':'0','len':vlen}
        json_foo = json.dumps(foo)
        connection.request('POST','/markdown',json_foo,headers)
        response = connection.getresponse()
    #    print(response.read().decode())
        
    def mytalk1(self,vlen):
        time.sleep(4)
        foo = {'text':'talk','angle':'0','len':vlen}
        json_foo = json.dumps(foo)
        connection.request('POST','/markdown',json_foo,headers)
        response = connection.getresponse()
        
rpi = rpi_interface()
rpi.talk(20)