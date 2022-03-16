import  random

s = "jonathanfulltmp"
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

    return  choices


listnum=choose_with_step(range(1,16), 4, 8)


for i in listnum:
    s = s[:i] + "." + s[i:]  # as suggested in your link
    # s = s.replace("..", "+")
    s = s.replace("..", ".")


finalemail=s+"@gmail.com"
print(finalemail)


