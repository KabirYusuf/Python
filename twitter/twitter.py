users = [
    {'name' : 'Hadiza',
     'age': 21,
     'gender': 'Female',
     'username': 'deezah',
     'is_verified': True,
     'tweets': [{'content': 'PO for President', 'likes': 450, 'retweet': 76},
                {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2},
                ]
     },

{'name' : 'Ibrahim',
     'age': 32,
     'gender': 'Male',
     'username': 'ibro',
     'is_verified': False,
     'tweets': [{'content': 'Programming is fun', 'likes': 34, 'retweet': 57},
                {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2},
                ]
     },

{'name' : 'James',
     'age': 25,
     'gender': 'Male',
     'username': 'amez',
     'is_verified': True,
     'tweets': [{'content': 'Love is life', 'likes': 6, 'retweet': 89},
                {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2},
                ]
     },

{'name' : 'Racheal',
     'age': 22,
     'gender': 'Female',
     'username': 'betty',
     'is_verified': True,
     'tweets': [{'content': '.', 'likes':1450, 'retweet': 1330},
                {'content': 'Thinking about amez', 'likes': 4, 'retweets': 2},
                {'content': 'Amazing grace', 'likes': 4, 'retweets': 2},
                ]
     },

{'name' : 'Elijah',
     'age': 17,
     'gender': 'Male',
     'username': 'el_d_si',
     'is_verified': False,
     'tweets': [{'content': '#Osun decides', 'likes': 12, 'retweet': 8},
                {'content': 'imole de', 'likes': 8, 'retweets': 1},
                ]
     },

{'name' : 'Dorris',
     'age': 16,
     'gender': 'Female',
     'username': 'anything',
     'is_verified': False,
     'tweets': [{'content': 'I love Chimamanda', 'likes': 40, 'retweet': 76},
                {'content': 'Feminism is the goal', 'likes': 4980, 'retweets': 27},
                ]
     },

{'name' : 'Jacob',
     'age': 37,
     'gender': 'Male',
     'username': 'elder_j',
     'is_verified': True,
     'tweets': [{'content': 'Reflection is my goal', 'likes': 5, 'retweet': 3},
                {'content': 'How to get more likes on twitter', 'likes': 1, 'retweets': 1},
                ]
     },

{'name' : 'Derrick',
     'age': 29,
     'gender': 'Male',
     'username': 'standby_gen',
     'is_verified': False,
     'tweets': [{'content': 'PO for President', 'likes': 450, 'retweet': '233'},
                {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2},
                ]
     },

{'name' : 'Mubarak',
     'age': 47,
     'gender': 'Male',
     'username': 'Whistle',
     'is_verified': True,
     'tweets': [{'content': 'PO for President', 'likes': 450, 'retweet': '233'},
                {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2},
                ]
     },
]

no_of_users = len(users)
usernames = {user['username'] for user in users}
print(usernames)
female_user = [user['name'] for user in users if user['gender'] == 'Female']
print(female_user)
inactive_user =[user for user in users if len(user['tweets']) == 0]
users_age_name = [{'name': user['name'], 'age': user['age']} for user in users]
print(users_age_name)
avg_age_of_users = round(sum(user['age'] for  user in users)/len(users))
print(avg_age_of_users)
print(max(users, key=lambda x: x['age']))
print(max(users, key=lambda x: len(x['tweets'])))

iterable1 = (1,2,3,4)
iterable2 = ('hello', 'how', 'are', 'you')
print(list(zip(iterable2,iterable1)))
print(dict(zip(iterable2,iterable1)))

print(sorted('hello'))
print(sorted('helloAZ', reverse= True))

print(sum(user['age'] for user in users) / len(users))

print(any(user['is_verified'] for user in users))
print(all(user['is_verified'] for user in users))