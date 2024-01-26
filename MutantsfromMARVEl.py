import random
import string
def string_mutants(a_string, prof_x):
    char_list = list(a_string)
    for i in range(prof_x):
        index_to_mutate = random.randint(0, len(char_list) - 1)
        new_char = random.choice(string.ascii_letters)
        char_list[index_to_mutate] = new_char
    mutated_string = ''.join(char_list)
    return mutated_string
a_string = input("#strings")
prof_x = int(input("#mutants"))
mutant_string = string_mutants(a_string, prof_x)
print("#puberty", mutant_string)