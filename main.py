import random

# why oop? brushing up on my oop skills in python 
# handles all the logic of the game
class Game:
    def __init__(self) -> None:
        self.round = 1
        self.winner = None
        self.game_over = False
    
    class player:
        def __init__(self,name) -> None:
            self.name = name
            self.move = None
            self.score = 0
        
        def won(self):
            self.score += 1
        
        def lost(self):
            self.score -= 1
    

    def make_move(self):
        return random.choice(['rock', 'paper', 'scissors'])


    def check_result(self, p1, p2) -> str:
        if p1.move == p2.move:
            return "tie"
                
        elif (p1.move == 'rock' and p2.move == 'paper') or \
                (p1.move == 'paper' and p2.move == 'scissors') or \
                (p1.move == 'scissors' and p2.move == 'rock'):

            p1.lost()
            p2.won()
            return "You lose!"
            
        
        else:
            p1.won()
            p2.lost()
            return "You win!"
            

    def play(self, player_name = None) -> None:
  
        print("{}\nRound {}".format('-'*35,self.round))
        
        choice = input("Please enter your move [Rock|Paper|Scissors]: ").lower()
        
        if choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice!")
            return

        player = Game.player("You") if player_name else Game.player(player_name)
        player.move = choice
        
        bot = Game.player("Bot 🤖")
        bot.move = self.make_move()

        print("Bot 🤖: {}".format(bot.move))
        
        result = self.check_result(player, bot)

        self.round += 1
        
        print(">> Result: {}".format(result))
    
        self.check_game_over(player, bot)
        
        if self.game_over:
            print('\n{} wins!'.format(self.winner))
            return

        print("Your Score: {}".format(player.score))


    def check_game_over(self, player, bot) -> None:
        if player.score < 0:
            self.winner = bot.name
            self.game_over = True
        
        elif player.score == 3:
            self.winner = player.name
            self.game_over = True
        elif bot.score == 3:
            self.winner = bot.name
            self.game_over = True

    
def main():
    game = Game()
    print("🪨 📄 ✂ Welcome to Rock, Paper, Scissors! 🪨 📄 ✂")
    player_name = input("[!] Name: ")

    while not game.game_over:
        game.play( None if player_name == "" else player_name )


if __name__ == "__main__":
    main()