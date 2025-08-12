players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(f'Here are the first three players on my team:')
for player in players[0:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

