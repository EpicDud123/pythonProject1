import random
import string
def generate_gamertag():
    text_length = random.randint(1, 10)
    random_text = ''.join(random.choice(string.ascii_letters) for i in range(text_length))
    result_text = "Xx" + random_text
    num_numbers = random.randint(2, 3)
    result_text += ''.join(random.choice(string.digits) for i in range(num_numbers))
    result_text += "xX"
    return result_text
random_text = generate_gamertag()
print(random_text)
