# 1.1 → Programa 4
from random import seed
from random import choice
seed(4106)
print(not (choice([True, False]) and choice([True, False])))


# 1.2 → Programa 2
from random import seed
from random import choice
seed(4106)
print(choice([True, False]) and choice([True, False]))


# 1.3 → Programa 5
from random import seed
from random import choice
seed(4106)
print(choice([True, False]) or (not choice([True, False])) or choice([True, False]))


# 1.4 → Programa 3
from random import seed
from random import choice
seed(4106)
print(choice([True, False]) or choice([True, False]))


# 1.5 → Programa 1
from random import seed
from random import choice
seed(4106)
print(not choice([True, False]))


# 2.1 → Programa 3
from random import seed
from random import randint
seed(5622)
print(randint(1, 100) > randint(1, 100))


# 2.2 → Programa 4
from random import seed
from random import randint
seed(5622)
print(randint(1, 100) >= randint(1, 100))


# 2.3 → Programa 5
from random import seed
from random import randint
seed(5622)
print(randint(1, 100) <= randint(1, 100))


# 2.4 → Programa 2
from random import seed
from random import randint
seed(5622)
print(randint(1, 100) != randint(1, 100))


# 2.5 → Programa 1
from random import seed
from random import randint
seed(5622)
print(randint(1, 100) == randint(1, 100))