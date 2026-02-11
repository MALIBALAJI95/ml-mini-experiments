import time

class RateLimiter:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_checked = time.time()

    def allow_request(self):
        now = time.time()
        elapsed = now - self.last_checked
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        self.last_checked = now

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
