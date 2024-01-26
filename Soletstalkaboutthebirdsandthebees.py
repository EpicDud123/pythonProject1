import random
def birdsplusbeesbutbetterinothercases(birds, bees):
    birees = ''
    for i in range(max(len(birds), len(bees))):
        if i < len(birds) and i < len(bees):
            birees += random.choice([birds[i], bees[i]])
        elif i < len(birds):
            birees += birds[i]
        else:
            birees += bees[i]
    return birees
def birdsplusbeesbutbetterinsomecases(birds, bees):
    birees = ''
    incursion=random.randint(0, min(len(birds), len(bees)))
    birees += birds[0:incursion]+bees[incursion:]
    return birees
print(birdsplusbeesbutbetterinsomecases("Nineteen","onehuned"))