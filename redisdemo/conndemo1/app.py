import os
import socket
from flask import Flask
from redis import Redis

app = Flask(__name__)
redisHost = os.environ.get('REDIS_HOST', '127.0.0.1')
print(redisHost)
redis = Redis(host=redisHost, port=6379)

@app.route('/')
def hello():
    redis.incr("hits")
    return 'hello world hit %s times host name is %s \n' % (redis.get('hits'), socket.gethostname())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)