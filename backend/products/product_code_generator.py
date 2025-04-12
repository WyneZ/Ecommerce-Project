import time
import random
import string


def generate_product_id(category_code):
    timestamp = int(time.time())
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"{category_code}-{timestamp}-{suffix}"

print(generate_product_id("COMP"))
print(type(generate_product_id("COM")))

