#exercise 3.4 inviting people
friends = ['brian' , 'adrian' , 'andi']
message = ' ,please come to my party thanks!'
for i in range (0,3):
    print(friends[i-1] + message)
print('\n\n\n')

#exercise 3.5 changing guest list
popfriends = friends.pop(0)
print(popfriends + ' cant come')
friends.append('lamin')
for i in range (1,4):
    print(friends[i-1] + message)
print('\n\n\n')

#exercise 3.6 adding people to parties
print('I have found a bigger table so....\n')
friends.insert(0,'brian')
friends.insert(2, 'krissy')
friends.append('Amanda')
x = len(friends)
for i in range (0,x+1):
    print(friends[i-1] + message)

#exercise 3.7 KICKING PEOPLE OUT OF MY PARTY

print('the table is canceled')
for i in range(2,x):
    friends.pop(2)
print('so only these 2 can come: ')
print(friends)
