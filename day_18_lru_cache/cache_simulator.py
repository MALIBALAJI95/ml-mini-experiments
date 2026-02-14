from lru_cache import LRUCache

cache = LRUCache(3)

cache.put(1, "User1")
cache.put(2, "User2")
cache.put(3, "User3")

print(cache.get(1))   # User1
cache.put(4, "User4") # removes key 2

print(cache.get(2))   # -1 (evicted)
print(cache.get(3))   # User3
print(cache.get(4))   # User4
