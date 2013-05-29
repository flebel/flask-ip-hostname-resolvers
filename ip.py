#!/usr/bin/env python

from flask import Flask, make_response, request
app = Flask(__name__)


@app.route('/')
def get_ip():
  response = make_response(request.remote_addr)
  response.mimetype = 'text/plain'
  return response


if __name__ == '__main__':
  app.run()
