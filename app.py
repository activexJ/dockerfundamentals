from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

import socket
import redis
import os
from dotenv import load_dotenv
import time

load_dotenv(verbose=True)

app = FlaskAPI(__name__)

print('Connecting to'+os.environ["REDIS_HOST"])
r = redis.Redis(host=os.environ["REDIS_HOST"], port= os.environ["REDIS_PORT"])
host = socket.gethostname();
if r.get(host) == None :
    r.set(host, 0) 

@app.route('/', methods=['GET'])
def index():
    time.sleep(1)
    visits = r.incr(host)
    return {'msg':'Hello World', 'host': host, 'totalVisits': visits}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')