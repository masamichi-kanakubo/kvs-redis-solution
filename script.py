import redis
import os
from dotenv import load_dotenv

load_dotenv()

host_client = os.environ.get('HOST_CLIENT')
redis_password = os.environ.get('REDIS_PASSWORD')
redis_port = os.environ.get('REDIS_PORT')

r = redis.Redis(
  host=host_client,
  port=33202,
  password=redis_password,
  ssl=True
)

r.set('foo', 'bar')
print(r.get('foo'))