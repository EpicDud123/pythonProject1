import numpy as np
import random
import string
import difflib
import Levenshtein


def get_random_character():
    return random.choice(string.ascii_letters + string.digits + string.punctuation + "\n" + " ")


def generate_random_string(length):
    return ''.join(get_random_character() for _ in range(length))


def string_similarity(str1, str2, mode="difflib"):
    mode=mode.lower()
    if mode=="difflib":
        return difflib.SequenceMatcher(None, str1, str2).ratio()
    elif mode=="levenshtein":
        return 1-Levenshtein.distance(str1, str2)/max(len(str1), len(str2))


def mutate_string(original, threat=0.1):
    mutated = list(original)
    for i in range(len(original)):
        if random.uniform(0, 1) < threat:
            mutated[i] = get_random_character()
    return ''.join(mutated)


def birdsplusbees(birds, bees):
    birees = ''
    incursion = random.randint(0, min(len(birds), len(bees)))
    birees += birds[0:incursion] + bees[incursion:]
    return birees

def Sogodhearmeoutherewhatifwegottheoldboringanimalsintheworldandhadthemadapttotheirenvirnmontsotheycanlivelongerandthesechangescouldbegoodorbadtothembutnothelessitwillalwayshappenliketakethetrexandwhatwemadeitsmallhavefeathersandabeakitsgenius(
        mutation_rate = 0.01,
        population_size = 1000,
        input_string="",
        District_1=0.5,
):
    generations = 0
    random_strings = [generate_random_string(len(input_string)) for _ in range(population_size)]
    while True:
        generations += 1
        similarities = [string_similarity(input_string, s, mode="Levenshtein") for s in random_strings]
        avg_fitness = np.mean(similarities)
        most_similar_string = random_strings[np.argmax(similarities)]

        if most_similar_string == input_string:
            print(f"Input string '{input_string}' found in generation {generations}")
            break
        sorted_indices = np.argsort(similarities)[::-1]
        top_half = sorted_indices[:int(population_size * District_1)]
        new_generation = []
        for i in range(population_size):
            parent1 = random_strings[top_half[random.randint(0, len(top_half) - 1)]]
            parent2 = random_strings[top_half[random.randint(0, len(top_half) - 1)]]
            offspring = birdsplusbees(parent1, parent2)
            new_generation.append(offspring)
        mutated_offspring = [mutate_string(child, threat=mutation_rate) for child in new_generation]
        random_strings = mutated_offspring[:]
        print(f"Generation: {generations}, Most similar: {most_similar_string}, Average fitness: {round(avg_fitness, 3)}, Inches: {len(new_generation)}")


if __name__ == "__main__":
    Sogodhearmeoutherewhatifwegottheoldboringanimalsintheworldandhadthemadapttotheirenvirnmontsotheycanlivelongerandthesechangescouldbegoodorbadtothembutnothelessitwillalwayshappenliketakethetrexandwhatwemadeitsmallhavefeathersandabeakitsgenius(
        population_size=1000, input_string="abc1dfg3abc1dfg2abc1dfg3abc1dfg2",
    )
    #4 characters=6
    #8 characters=13
    #16 characters=23
    #32 characters=45