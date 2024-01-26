import random
import string
Gamertag = input("input the base text you want your gamertag to be")
def generate_gamertag():
    result_text = "Xx" + Gamertag
    num_numbers = random.randint(2, 3)
    result_text += ''.join(random.choice(string.digits) for i in range(num_numbers))
    result_text += "xX"
    return result_text
Gamertag = generate_gamertag()
print(Gamertag)