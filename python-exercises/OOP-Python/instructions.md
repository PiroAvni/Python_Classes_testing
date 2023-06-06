# Python OOP Exercises

Practice of OOP principles in Python

## Organisation

### Duration

Two exercises:

- Exercise #1: 1h
- Exercise #2: 1h

Note that times are approximate and you can decide how much time you spend on each exercise

Make sure to take breaks!

### Team

Same pairs of the previous day

## Brief

### Exercise #1

Using classes, **create** a fighting game for 2 users, following these requirements:

- You must at least create 5 different characters (different stats, names ...)
- Players can choose a character each
- Each character must have an attack move and a defense move
- Each character must have a special unique attack on top of the attack move
- Each character must have a certain amount of health points and energy points (can vary per character but make them balanced)
- The game happens in turns, each character introduces what they want to do in the next move (attack, defend or special attack), the outcome is calculated, their points are updated and the updates displayed in the terminal before the next round (if there is one). 
- There must be a winner and a loser to the game and a special message for each. 

**Example:**

- Player 1 attacks
- Player 2 defends

(calculating...)

- Player 1 has lost 5 energy points
- Player 2 has lost 1 health point

---------------

- Player 1 attacks
- Player 2 attacks

(calculating...)

- Player 1 has lost 10 health points
- Player 2 has lost 15 health points 

----------------

- Player 1 attacks
- Player 2 attacks with special move

(calculating)

- Player 1 has lost 30 health points
- Player 2 has lost 15 health points

- Player 1 is unconscious
- Player 2 wins the game!

### Exercise #2

- **Create** a CLI with an Object Oriented design
  - On starting the app, User is asked for their GitHub username
  - A request is made to `https://api.github.com/users/<username>/repos`
  - API data is turned into instances of Repository class
  - User is shown a numbered list their repos by name
  - User can input a number to see more details on the corresponding repository

---

[Back](./README.md)

---