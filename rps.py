def play_rps(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'paper' and player2_choice == 'rock') or \
         (player1_choice == 'scissors' and player2_choice == 'paper'):
        return "Naruto wins!"
    else:
        return "Kurama wins!"

def main():
    print("Let's play Rock-Paper-Scissors!")
    naruto = input("Naruto, enter your choice (rock, paper, or scissors): ").lower()
    kurama = input("Kurama, enter your choice (rock, paper, or scissors): ").lower()

    while naruto not in ['rock', 'paper', 'scissors'] or kurama not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
        naruto = input("Naruto, enter your choice (rock, paper, or scissors): ").lower()
        kurama = input("Kurama, enter your choice (rock, paper, or scissors): ").lower()

    print(play_rps(naruto, kurama))

if __name__ == "__main__":
    main()
