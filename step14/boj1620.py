import sys

N, M = map(int, sys.stdin.readline().split())

pokemon = dict()
pokemon_rev = dict()

for i in range(N) :
    pokemon_name = sys.stdin.readline().strip()
    pokemon[str(i+1)] = pokemon_name
    pokemon_rev[pokemon_name] = str(i+1)

for i in range(M) :
    myinput = sys.stdin.readline().strip()
    if myinput in pokemon :
        print(pokemon[myinput])
    else :
        print(pokemon_rev[myinput])