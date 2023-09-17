class GameState:
    """Organizes game loop."""
    SELECTING = 0
    FIGHTING = 1

class Duck:
    ACTION_READY = 10
    def __init__(self, name):
        self.hp = int(input('HP for {}: \n'.format(name)))
        self.damage = int(input('Damage for {}: \n'.format(name)))
        self.speed = int(input('Speed for {}: \n'.format(name)))
        self.action_step = 0

        self.cards = ["Increase HP " + name, "Speed Boost " + name, name + "S1", name + "S2", name + "S3"]
        self.currCardIndex = 0

    def step(self):
        self.action_step += self.speed
    
    def act(self, otherDuck):
        if self.action_step >= Duck.ACTION_READY:
            self.action_step = 0
            # Play card actions here.
            if self.currCardIndex < len(self.cards):
                print(self.cards[self.currCardIndex])
                self.currCardIndex += 1
            # ideas: have a list of cards that ducks hold
            # and 'play' the corresponing card here.
            # will need the cards to manage themselves from here on out.
            otherDuck.hp -= self.damage
            return self.cards[self.currCardIndex - 1]
        return "None"
    
    def dead(self):
        return self.hp <= 0

class GameManager:
    def __init__(self):
        """Called once before loop."""
        self.game_state = GameState.SELECTING

    def endTurn(self):
        """Called at the end of every turn."""
        # self.duck1LastPlayedCard.finish()
        print(self.duck1LastPlayedCard)
        print(self.duck2LastPlayedCard)
        pass

    def startTurn(self):
        pass

    def update(self):
        """Updated every frame."""
        match self.game_state:
            case GameState.SELECTING:
                print("Selecting")
                self.Duck1 = Duck("1")
                self.Duck2 = Duck("2")
                self.game_state = GameState.FIGHTING
            case GameState.FIGHTING:
                print("Fighting")

                self.startTurn()

                self.Duck1.step()
                self.Duck2.step()

                # Make this action random so if they are ready at the same time there is
                # some luck to it.
                self.duck1LastPlayedCard = self.Duck1.act(self.Duck2)
                self.duck2LastPlayedCard = self.Duck2.act(self.Duck1)

                self.endTurn()

                print(self.Duck1.hp)
                print(self.Duck2.hp)

                if self.Duck1.dead():
                    print("Game Over! Duck2 Won!")
                    exit(0)

                if self.Duck2.dead():
                    print("Game Over! Duck1 Won!")
                    exit(0)

    
