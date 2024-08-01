class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reserse_linked_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


class cache:
    def __init__(self):
        self.cache = {}
    def get(self, key):
        return self.cache.get(key, None)
    def set(self, key, value):
        self.cache[key] = value
    def delete(self, key):
        if self.cache.__contains__(key):
            del self.cache[key]
        return
    
    
import time
from collections import deque

characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_map = {i: char for i, char in enumerate(characters)}

def base62_encode(num):
    if num == 0:
        return characters[0]

    base = len(characters)
    encoded_str = deque()
    
    while num > 0:
        num, rem = divmod(num, base)
        encoded_str.appendleft(char_map[rem])
    
    # Convert deque to string
    encoded_str = ''.join(encoded_str)
    
    # Pad with leading zeros to ensure length is 7
    while len(encoded_str) < 7:
        encoded_str = characters[0] + encoded_str
    
    return encoded_str

# Get current timestamp
timestamp = int(time.time()*1000)

# Convert timestamp to base62 and ensure length is exactly 7
base62_str = base62_encode(timestamp)

print(f"Timestamp: {timestamp}")
print(f"Base62: {base62_str}")



