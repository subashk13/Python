import random
import string

length=int(input("Enter Password Length:"))

lower=string.ascii_lowercase
upper=string.ascii_lowercase
digits=string.digits
special=string.punctuation

password=[
    random.choice(lower),
    random.choice(upper),
    random.choice(digits),
    random.choice(special)
]

all_chars=lower+upper+digits+special
for _ in range(length-4):
    password.append(random.choice(all_chars))

random.shuffle(password)

final_password="".join(password)

print("Generated Password:",password)