from rate_limiter import RateLimiter
import time

limiter = RateLimiter(rate=2, capacity=5)  # 2 requests per second, max 5 burst

for i in range(10):
    if limiter.allow_request():
        print("Request", i+1, "→ Allowed")
    else:
        print("Request", i+1, "→ Blocked")
    time.sleep(0.3)
