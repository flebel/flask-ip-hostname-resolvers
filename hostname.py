#!/usr/bin/env python

import socket

from flask import Flask, make_response, request
app = Flask(__name__)


@app.route('/')
def get_hostname():
  if hasattr(socket, 'setdefaulttimeout'):
    socket.setdefaulttimeout(5) # Seconds
  hostname = socket.gethostbyaddr(request.remote_addr)
  response = make_response(hostname[0])
  response.mimetype = 'text/plain'
  return response


if __name__ == '__main__':
  app.run()
