import redis
import ssl
import os
from dotenv import load_dotenv
import time

load_dotenv()

host_client = os.environ.get('HOST_CLIENT')
redis_password = os.environ.get('REDIS_PASSWORD')
redis_port = os.environ.get('REDIS_PORT')

redis_client = redis.Redis(
  host=host_client,
  port=33202,
  password=redis_password,
  ssl=True,
  ssl_cert_reqs=ssl.CERT_NONE
)

redis_client.set('count', 0)
while True:
    count = int(redis_client.get('count'))

    count += 1
    print(count)
    redis_client.set('count', count)

    time.sleep(10)
