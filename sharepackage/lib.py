import random
import string

characters = string.ascii_letters+string.digits+string.punctuation
def try_me(random_seed=420):
    emptystr = ''
    random.seed(random_seed)
    for i in range(30):
        emptystr += characters[random.randint(0, len(characters)-1)]
    return emptystr

if __name__ == "__main__":
    # Le Wagon location
print('Call try_me() with any random number to generate a random 30 character password')     