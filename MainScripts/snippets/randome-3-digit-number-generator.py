import random


def choose_with_step(domain, step, k):
    domain = list(domain)
    random.shuffle(domain)
    exclusions = set()
    choices = []

    while domain and k > 0:
        choice = domain.pop()

        if choice not in exclusions:
            choices.append(choice)
            for x in range(choice - step + 1, choice + step):
                exclusions.add(x)

            k -= 1

    print(choices)
choose_with_step(range(16), 2, 6)