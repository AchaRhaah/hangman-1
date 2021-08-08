import random


stages=['''+----+
           |     |
           O     |
          /|\    |
          / \    |
==================         
                ''',
''''                
           +----+
           |     |
           O     |
          /|\    |
          /      |
==================         
                ''',
                ''''                
           +----+
           |     |
           O     |
          /|\    |
                 |
==================         
                ''',
                ''''                
           +----+
           |     |
           O     |
          /|     |
                 |
==================         
                ''',
                ''''                
           +----+
           |     |
           O     |
           |     |
                 |
==================         
                ''',
                ''''                
           +----+
           |     |
           O     |
                 |
                 |
==================         
                ''',
                ''''                
           +----+
           |     |
                 |
                 |
                 |
==================         
                ''',
]

import random
display=[]

word_list=['apple','banana','orange']

choosen_word=random.choice(word_list)
print(choosen_word)

lives=6
for position in range(len(choosen_word)):
  display+='_'
  end_of_game = False
while not end_of_game :
  guess=input('guess a letter:').lower()
  for position in range(len(choosen_word)):
    letter=choosen_word[position]
    if letter==guess:
      display[position]=letter
  

  if guess not in choosen_word:
      lives-=1
      print(lives)
  print(stages[lives])
  
  
    
  print(f"{''.join(display)}")  


  if '_' not in display:
    end_of_game = True
    print('you win')     

  


      
      
  
  


  

