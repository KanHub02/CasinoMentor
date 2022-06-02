from random import randint, choice
import time


class Bank:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def game_logic(self):
        while self.balance != 0 or self.balance < 0:
            bet = int(input('Your Bet?'))
            if bet < self.balance or bet == self.balance:
                lots = [5, 10, 15, 20]
                task = int(input(f'Choose lot from {lots}'))
                winlot = choice(lots)
                if task == winlot:
                    self.balance += bet
                    print('You Win!!')
                    time.sleep(0.5)
                    print(f'Your Balance{self.balance}')
                    continue
                elif task != winlot:
                    self.balance -= bet
                    print('You lose!!')
                    time.sleep(0.5)
                    print(f'{self.username}, Your Balance {self.balance}')
                    continue
            else:
                print(f'No money enough {self.username}')
            continue


Player1 = Bank('Kanat', 1000)
Bank.game_logic(Player1)
print(Player1.balance)