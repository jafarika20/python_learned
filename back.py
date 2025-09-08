import random
import string
password=random.sample(string.ascii_uppercase + string.digits+ string.ascii_lowercase,12)
print(''.join(password))
