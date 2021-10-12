# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 13:24:23 2021

@author: Robot 2
"""

from __future__ import division
from http.server import BaseHTTPRequestHandler, HTTPServer
import os,time,random,sys
from multiprocessing import Process
from subprocess import check_output
from subprocess import Popen, PIPE
from mutagen.mp4 import MP4
import subprocess
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
import json,os

from time import sleep
import cv2
import numpy as np
import time
 
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        print(parsed_path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version
        }).encode())
        return

    def do_POST(self):
        content_len = int(self.headers.get('content-length'))
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body.decode('utf-8'))
        print(data)
        if 'len' in data:
            vlen = data['len']
        else:
            vlen = 0
        if data['text'].lower() == 'shutdown':
            self.shutdown()
        elif data['text'].lower() == 'restart':
            self.restart()
        elif data['text'].lower() == 'mode':
            if 'mode_val' in data:
                if data['mode_val'] == 'gen':
                    self.lesson(vlen)
                elif data['mode_val'] == 'les':
                    self.lesson(vlen)
                elif data['mode_val'] == 'wrg':
                    self.wrong(vlen)
                elif data['mode_val'] == 'err':
                    self.error(vlen)
                elif data['mode_val'] == 'rgt':
                    self.right(vlen)
                elif data['mode_val'] == 'think':
                    self.think(vlen)
                elif data['mode_val'] == 'assess':
                    self.assisment(vlen)    
                    
                    
        parsed_path = urlparse(self.path)
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version,
            'body': data
        }).encode())
        return

    
    def shutdown(self):
        pi.stop()
        os.system('sudo shutdown -r now')
        
    def restart(self):
        pi.stop()
        os.system("sudo reboot")

    def blue_on(self,vlen):
        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture('TechFailure.jpg')
         
        # Check if camera opened successfully
        if (cap.isOpened()== False):
            print("Error opening video file")
            
        start_time = time.time()

        # Read until video is completed
        while(int(time.time()-start_time) < vlen):
            
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv2.namedWindow ('Frame', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty ('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                #cv2.resizeWindow("output", 640, 480)
                frame = cv2.resize(frame, (800, 480))
#                 imS = cv2.resize(im, (640, 480)) 
                cv2.imshow('Frame', frame)
                

                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break

        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()

    #def blue_off(self):
    #    pi.set_PWM_dutycycle(24, 0)

        
    def assess_on(self,vlen):
        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture('Green.mp4')

        # Check if camera opened successfully
        if (cap.isOpened()== False):
            print("Error opening video file")
        
        start_time=time.time()

        # Read until video is completed
        while(int(time.time()-start_time) < vlen):
            
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv2.namedWindow ('Frame', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty ('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                #cv2.resizeWindow("output", 640, 480)
                frame = cv2.resize(frame, (800, 480))
                cv2.imshow('Frame', frame)
#                 imS = cv2.resize(im, (640, 480)) 
                  #cv2.imshow('Frame', frame)
                

                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break

        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()

        
    #def green_off(self):
    #    pi.set_PWM_dutycycle(17, 0)

        
    def purple_on(self,vlen):
        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture('purplesad.mp4')

        # Check if camera opened successfully
        if (cap.isOpened()== False):
            print("Error opening video file")
            
        start_time = time.time()

        # Read until video is completed
        while(int(time.time()-start_time) < vlen):
            
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv2.namedWindow ('Frame', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty ('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                #cv2.resizeWindow("output", 640, 480)
                frame = cv2.resize(frame, (800, 480))
                cv2.imshow('Frame', frame)
#                 imS = cv2.resize(im, (640, 480)) 
                #cv2.imshow('Frame', frame)

                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break

        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()

    #def red_off(self):
    #    pi.set_PWM_dutycycle(22, 0)


    def yellow_on(self,vlen):
        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture('yellow.mp4')

        # Check if camera opened successfully
        if (cap.isOpened()== False):
            print("Error opening video file")
            
        start_time = time.time()

        # Read until video is completed
        while(int(time.time()-start_time) < vlen):
            
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv2.namedWindow ('Frame', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty ('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                #cv2.resizeWindow("output", 640, 480)
                frame = cv2.resize(frame, (800, 480))
                cv2.imshow('Frame', frame)
#                 imS = cv2.resize(im, (640, 480)) 
                #cv2.imshow('Frame', frame)

                #Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break

        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()

#    def yellow_off(self):
#        pi.set_PWM_dutycycle(17, 0)
#        pi.set_PWM_dutycycle(22, 0)
#        pi.set_PWM_dutycycle(24, 0)

    def general(self,vlen):
        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture('Green.mp4')

        # Check if camera opened successfully
        if (cap.isOpened()== False):
            print("Error opening video file")
            
        start_time = time.time()

        # Read until video is completed
        while(int(time.time()-start_time) < vlen):
            
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv2.namedWindow ('Frame', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty ('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                #cv2.resizeWindow("output", 640, 480)
                frame = cv2.resize(frame, (800, 480))
                cv2.imshow('Frame', frame)
#                 imS = cv2.resize(im, (640, 480)) 
                #cv2.imshow('Frame', frame)

                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break

        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()
        
    def assess_on(self,vlen):
        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture('GreenSmile.mp4')

        # Check if camera opened successfully
        if (cap.isOpened()== False):
            print("Error opening video file")
            
        start_time = time.time()

        # Read until video is completed
        while(int(time.time()-start_time) < vlen):
            
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv2.namedWindow ('Frame', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty ('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                #cv2.resizeWindow("output", 640, 480)
                frame = cv2.resize(frame, (800, 480))
                cv2.imshow('Frame', frame)
#                 imS = cv2.resize(im, (640, 480)) 
                #cv2.imshow('Frame', frame)

                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break

        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()    
    
    def orange_on(self,vlen):
        import os
        cwd = os.getcwd()
        print(cwd)
        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture('Orangethinking.mp4')
        print(cap,cap.isOpened())
        # Check if camera opened successfully
        if (cap.isOpened()== False):
            print("Error opening video file")
            
        start_time = time.time()

        # Read until video is completed
        while(int(time.time()-start_time) < 20):
            
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv2.namedWindow ('Frame', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty ('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                #cv2.resizeWindow("output", 640, 480)
                frame = cv2.resize(frame, (800, 480))
                cv2.imshow('Frame', frame)
#                 imS = cv2.resize(im, (640, 480)) 
                #cv2.imshow('Frame', frame)

                #Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break

        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()


    def lesson(self,vlen):
        self.yellow_on(vlen)
        #time.sleep(int(vlen))
        #self.green_off()

    def wrong(self,vlen):
        self.purple_on(vlen)
        #time.sleep(int(vlen))
        #self.blue_off()

    def error(self,vlen):
        self.blue_on(vlen)
        #time.sleep(int(vlen))
        #self.red_off()
        
    def right(self,vlen):
        self.green_on(vlen)
        
        
    def think(self,vlen):
        self.orange_on(vlen)
        
    def assisment(self,vlen):
        self.assess_on(vlen)    


def freeport(port):
    try:
        port = int(port)
        cmd = 'lsof -t -i:{0}'.format(port)
        pid = None
        try:
            pid = subprocess.check_output(cmd, shell=True)
        except Exception as e:
            print("No process running on port {} by current user. Checking if root is running the proecess".format(port))
            if pid is None:
                cmd = 'sudo lsof -t -i:{0}'.format(port)
                pid = subprocess.check_output(cmd, shell=True)
        pids =  pid.decode().split("\n")
        pids_int = []
        for pid in pids:
            if pid:
                pid = int(pid)
                pids_int.append(pid)
        for pid in pids_int:
            processTypeCmd = 'ps -p {0} -o comm='.format(pid)
            processType = subprocess.check_output(processTypeCmd, shell=True, text=True).rstrip('\n')
            confirm = ''
            if processType:
                userCmd = 'ps -o user= -p {}'.format(pid)
                user = subprocess.check_output(userCmd, shell=True, text=True).rstrip('\n')
                if user.lower() == "root":
                    killCmd = 'sudo kill -9 {0}'.format(pid)
                else:
                    killCmd = 'kill -9 {0}'.format(pid)
                isKilled = os.system(killCmd)
                if isKilled == 0:
                    print("Port {0} is free. Processs {1} killed successfully".format(port, pid))
                else:
                    print("Cannot free port {0}.Failed to kill process {1}, err code:{2}".format(port, pid, isKilled))
    except ValueError as e:
        print(e)
        #exit()
    except Exception as e:
        print("No process found running on port {0}.".format(port))
        #exit()
    
    
    


if __name__ == '__main__':
##    try:
    ipaddr = None
    sleep(5)
    while True:
        try:
            ipaddr = str(check_output(['hostname', '--all-ip-addresses'])).replace("b'","").replace(" \\n'","").replace(" \n'","")
            print(ipaddr)
            if ipaddr != None:
                break
        except:
            print ("no ip found")
        time.sleep(1)
    print ("ip address:",ipaddr)
    for i in range(2):
        freeport(8181)
        if i > 0:
            try:
                server = HTTPServer((ipaddr, 8181), RequestHandler)
                print('Starting server at http://'+ipaddr)
                server.serve_forever()
            except Exception as e:
                server = HTTPServer((ipaddr, 8181), RequestHandler)
                print('Starting server at http://'+ipaddr)
                server.serve_forever()
            except:
                pass
    
        
    
    
