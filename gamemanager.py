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

    def step(self):
        self.action_step += self.speed
    
    def act(self, otherDuck):
        if self.action_step >= Duck.ACTION_READY:
            self.action_step = 0
            # Perform card actions here.
            otherDuck.hp -= self.damage
    
    def dead(self):
        return self.hp <= 0

class GameManager:
    def __init__(self):
        """Called once before loop."""
        self.game_state = GameState.SELECTING

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
                self.Duck1.step()
                self.Duck2.step()
                # Make this action random so if they are ready at the same time there is
                # some luck to it.
                self.Duck1.act(self.Duck2)
                self.Duck2.act(self.Duck1)

                print(self.Duck1.hp)
                print(self.Duck2.hp)

                if self.Duck1.dead():
                    print("Game Over! Duck2 Won!")
                    exit(0)

                if self.Duck2.dead():
                    print("Game Over! Duck1 Won!")
                    exit(0)

    
