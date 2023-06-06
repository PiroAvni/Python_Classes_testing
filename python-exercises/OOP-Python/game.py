class Character:
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy

    def attack(self):
        return 10

    def defend(self):
        return 5

    def special_attack(self):
        return 20


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        while self.player1.health > 0 and self.player2.health > 0:
            print(f"\n{self.player1.name} attacks")
            print(f"{self.player2.name} defends")
            self.calculate_outcome(self.player1, self.player2)

            if self.player2.health <= 0:
                break

            print(f"\n{self.player2.name} attacks")
            print(f"{self.player1.name} defends")
            self.calculate_outcome(self.player2, self.player1)

        self.display_results()

    def calculate_outcome(self, attacker, defender):
        attack_damage = attacker.attack()
        defense_points = defender.defend()
        damage_taken = max(0, attack_damage - defense_points)
        defender.health -= damage_taken

        print("\nCalculating outcome...")
        print(f"{attacker.name} has lost {attacker.energy} energy points")
        print(f"{defender.name} has lost {damage_taken} health points")

    def display_results(self):
        if self.player1.health <= 0 and self.player2.health <= 0:
            print("\nIt's a tie!")
        elif self.player1.health <= 0:
            print(f"\n{self.player1.name} is unconscious")
            print(f"{self.player2.name} wins the game!")
        else:
            print(f"\n{self.player2.name} is unconscious")
            print(f"{self.player1.name} wins the game!")


# Create characters
Ken = Character("Player 1", 100, 50)
Ryu = Character("Player 2", 100, 50)

# Start the game
game = Game(Ken, Ryu)
game.play()
