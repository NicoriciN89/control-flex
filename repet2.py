user = {
    'username': 'janpin',
    'online': True,
    'email': 'janpin@gmail.com',
    'rating': 1000,
    'friends': [
        'maria', 
        'candru', 
        'pentru', 
        'nicu',
        'andrei']
}

print("Username:", user['username'])
print("Email:", user['email'])
print("Rating:", user['rating'])
print('Friends list:')

for friend in user['friends']:
    print('>>', friend)

# Input more friends
num_new_friends = int(input("Enter the number of new friends you want to add: "))

for _ in range(num_new_friends):
    new_friend = input("Enter the name of a new friend: ")
    user['friends'].append(new_friend)

print('\nUpdated Friends list:')
for friend in user['friends']:
    print('>>', friend)

# Arithmetic based on rating
threshold_rating = 900

if user['rating'] > threshold_rating:
    user['rating'] += 100
    print("Rating increased by 100.")
else:
    user['rating'] -= 50
    print("Rating decreased by 50.")

print("New Rating:", user['rating'])
