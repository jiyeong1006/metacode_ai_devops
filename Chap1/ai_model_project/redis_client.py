import redis

# Redis 클라이언트 설정
redis_client = redis.Redis(host="redis", port=6379, db=0)

# 콜론이 반드시 필요합니다!
def set_key_value(key: str, value: str):
    redis_client.set(key, value)

def get_key_value(key: str):
    return redis_client.get(key)
