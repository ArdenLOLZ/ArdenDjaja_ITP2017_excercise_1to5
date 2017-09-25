#pizza list 4.1 writing pizza
pizzas = ['cheese', 'meat_lover','american_favorite' ]
for pizza in pizzas:
    print('i like ' +pizza.title() + 'pizza')
print('i really like pizza.' +'\ni really really like pizza.\n'+'i like peperoni pizza.\n\n\n')
print('\n\n\n')
# exercise 4.2 animal list
animal = ['snake','crocodile','iguana']
for animal in animal:
    print(animal.title()+' would make a great pet')
print('these animals are reptiles')
print('\n\n\n')
#exercise 4.3 counting to 20
twenty = list(range(1,21))
for twenty in range(1,21):
    print (twenty)
    print('\n\n\n')
#exercise 4.4 and 4.5 the 1 million
number = list(range(1,1000001))
print(min(number))
print (max(number))
print(sum(number))
print('\n\n\n')

#exercise 4.6 odd number listing
for twenty in range (1,21,2):
    print(twenty)
print('\n\n\n')
#exercise 4.7 the threes
thirty = list(range(1,31))
threes= []
for i in range(1,31):
    if(i%3==0):
        threes.append(i)
    else:
        continue
print(threes)
print('\n\n\n')
#exercise 4.8 cubes
cubes = [thirty**3 for thirty in range(0,11)]
for i in range(1,11):
    print (cubes[i])
print('\n\n\n')
#exercise 4.9 comprehension list
print(cubes)
print('\n\n\n')

#exercise 4.10 new test
listing = ['a','b','c','d','e']
print('the first 3 item: ')
print(listing[0:3])
print('the middle 3 item: ')
print(listing[1:4])
print('the last 3 item: ')
print(listing[2:5])
print('\n\n\n')

#exercise 4.11 friend's pizza
friend_pizza = pizzas[:]
pizzas.append('peperoni')
friend_pizza.append('super supreme')
print("My favorite pizzs are:")
for i in range (len(pizzas)):
    print(pizzas[i])
print("\nMy friend's favorite pizzas are:")
for i in range (len(friend_pizza)):
    print(friend_pizza[i])
print("\n\n\n")
#exercise 4.12 more loops
#but i already use loops up there for most of them

#exercise 4.13
restaurant =('pizza', 'spaghetti', 'caviar', 'sushi', 'steak')
for food in restaurant:
    print(food)
#restaurant[0] = 'curry'
#^^^^^ changing it for 4.13 assignment, please remove # to test
restaurant =('pizza', 'spaghetti', 'lasagna', 'curry', 'steak')
print('\n')
for food in restaurant:
    print(food)
#well i set everything for 4.15 and 4.14 so i guess it works
