#exercise 3.8 sorting exercise
places = ['pool','park','mountain','sea','hotel']
print(places)
print(sorted(places))
#prints again to show its not changed
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.reverse()
print(places)
print('\n\n\n')

#exercise 3.9 the Dinner Guest REMOVING PRINT FROM 3.4 TO 3.7
#------------------------------------------------------------------------------------------
#exercise 3.4 inviting people
friends = ['brian' , 'adrian' , 'andi']
message = ' ,please come to my party thanks!'
#for i in range (0,3):
    #print(friends[i-1] + message)
#print('\n\n\n')

#exercise 3.5 changing guest list
popfriends = friends.pop(0)
#print(popfriends + ' cant come')
friends.append('lamin')
#for i in range (1,4):
    #print(friends[i-1] + message)
#print('\n\n\n')

#exercise 3.5 adding people to parties
friends.insert(0,'brian')
friends.insert(2, 'krissy')
friends.append('Amanda')
x = len(friends)
#for i in range (0,x+1):
    #print(friends[i-1] + message)
#--------------------------------------------------------------------------------------------
numberofpeople = len(friends)
print('number of people going to party = ' + str(numberofpeople))
print('\n\n\n')


#exercise 3.10 please "BEAR" with me sir
bear = ['pooh bear','yogi bear','black bear', 'bear grillz']
print(bear)
print('can be sorted alphabetically to:')
print(sorted(bear))
bear.sort()
bear.reverse()
print('or the other way around as:')
print(bear)
popbear = bear.pop(3)
print(popbear + ' is a musician so we shall remove him and add jelly bear')
bear.append('jelly bear')
print(bear)
print('but lets just remove black bear too since he is a singer and add Pedobear')
bear.remove('black bear')
bear.insert(0,'Pedobear')
print(sorted(bear))

#exercise 3.11 INTENTIONAL ERROR????
#i added too many at the for() function and i think i got index error due to that misclick from 10 instead of 1
