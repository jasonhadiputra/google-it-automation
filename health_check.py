#!/usr/bin/env python3

import os
import shutil
import psutil
import socket
import emails

def cpu_usage_healthy():
  usage = psutil.cpu_percent(1)
  return usage < 80

def disk_space_healthy(disk):
  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free > 20

def memory_availability_healthy():
  available_memory = psutil.virtual_memory().available/(1024*1024)
  return available_memory > 500

def localhost_resolve_healthy():
  localhost = socket.gethostbyname('localhost')
  return localhost == '127.0.0.1'

tests = {
  cpu_usage_healthy(): "CPU usage is over 80%",
  disk_space_healthy("/"): "Available disk space is less than 20%",
  memory_availability_healthy(): "Available memory is less than 500MB",
  localhost_resolve_healthy(): "localhost cannot be resolved to 127.0.0.1"
}

error = False
for healthy, message in tests.items():
  if not healthy:
    error_message = message
    error = True

if error:
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Error - {}".format(error_message)
  body = "Please check your system and resolve the issue as soon as possible"
  message = emails.generate_error_report(sender, receiver, subject, body)
  emails.send_email(message)
  print('test')
