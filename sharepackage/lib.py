import random
import string
characters = string.ascii_letters+string.digits+string.punctuation
def try_me(random_seed=420):
    emptystr = ''
    random.seed(random_seed)
    for i in range(12):
        emptystr += characters[random.randint(0, len(characters)-1)]
    return emptystr
      