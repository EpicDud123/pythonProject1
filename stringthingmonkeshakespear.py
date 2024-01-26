import numpy as np
import random
import string
import difflib
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))
def string_similarity(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).ratio()
def mutate_string(original, threat=0.1):
    mutated = list(original)
    for i in range(len(original)):
        if random.uniform(0,1)<threat:
            mutated[i] = random.choice(string.ascii_letters)
    return ''.join(mutated)


if __name__ == "__main__":
    mutation_rate = 0.1
    input_string = "theresonehundred"
    random_strings = [generate_random_string(len(input_string)) for i in range(1000)]
    counter = 0
    while True:
        counter +=1
        most_similar_string = max(random_strings, key=lambda s: string_similarity(input_string, s))
        avg_fitness = np.mean([string_similarity(input_string, s) for s in random_strings])
        print(most_similar_string, f"Gen: {counter}", f"Average fitness: {avg_fitness}")
        if most_similar_string == input_string:
            print(input_string)
            break
        for i in range(1000):
            random_strings[i] = mutate_string(most_similar_string, threat=mutation_rate)