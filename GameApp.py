# FINAL VERSION
# Implement these features:
# A class, Enemy, that starts with three lives.
# A method to attack the enemy and reduce its life count by one.
# A method to check the enemy’s life count and either report when the enemy loses a life, or report that the enemy is dead.
# Generate three instances of the enemy in the program and attack the enemies to reduce their life count.

# class Enemy
class Enemy:
    lives = 3
    def attack(self):
        while True:
            play = input('Press return key to attack. ')
            if play == '':
                break
        r = random.randint(0,1)
        if r == 1:
            print("Ouch! That's a hit!")
            self.lives -= 1
            if self.lives == 1:
                print(f'This enemy has {self.lives} life left')
            else:
                print(f'This enemy has {self.lives} lives left')
        else:
            print("Haha!  Missed!  Try again.")
            return False
    def checkLife(self):
        if self.lives == 0:
            print("This enemy is dead!")
            return False

class Player:
    lives = 9
    def __init__(self, name):
        self.name = name
    def hi_player(self):
        print(f'Hi {self.name}!')
    def checkLife(self):
        self.lives -= 1
        if self.lives == 0:
            print(f"Hard luck {self.name}, you've lost all your lives.  Better luck next time!")
            quit()
        elif self.lives == 1:
            print(f'You have {self.lives} life left.')
        else:
            print(f'You have {self.lives} lives left.')

# intro
import random
print('''In this game you will confront three enemies, each with three lives.
Your task is to eliminate each enemy to win the game.
You will begin with 9 lives.  Each time you miss an enemy, you will lose a life.''')
player = Player(input("OK, so what's your name? "))
player_lives = player.lives
player.hi_player()
for i in range(3):
    print('Here comes enemy number ' + str(i + 1))
    enemy = Enemy()
    lives = enemy.lives
    while True:
        hit = enemy.attack()
        if hit == False:
            player.checkLife()
        else:
            play = enemy.checkLife()
            if play == False:
                break

print("Well done, you have defeated three enemies.  Now take a break and relax!")