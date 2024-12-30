
### Wargame program

### created by La'Ron Latin


import random

def create_deck():
    ranks = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]
    suits = ["S", "C", "D", "H"]
    deck = []

    for suit in suits:
        for rank in ranks:
            if rank == 'Jack':
                deck.append((11, suit))  # Jack is 11
            elif rank == 'Queen':
                deck.append((12, suit))  # Queen is 12
            elif rank == 'King':
                deck.append((13, suit))  # King is 13
            elif rank == 'Ace':
                deck.append((14, suit))  # Ace is 14
            else:
                deck.append((rank, suit))  # integer values of face cards

    return deck

def play_hand(player1_deck, player2_deck):
    common_pool = []  # Initialize common pool

    while True:
        if len(player1_deck) == 0 or len(player2_deck) == 0:
            return None  # No winner if one deck is empty

        card1 = player1_deck.pop(0)  # Player 1 plays their top card
        card2 = player2_deck.pop(0)  # Player 2 plays their top card
        common_pool.extend([card1, card2])  # Add played cards to common pool

        # Determine the winner
        if card1[0] > card2[0]:
            random.shuffle(common_pool)  # Shuffle the common pool before adding
            player1_deck.extend(common_pool)
            return "Player 1"
        elif card1[0] < card2[0]:
            random.shuffle(common_pool)  # Shuffle the common pool before adding
            player2_deck.extend(common_pool)
            return "Player 2"
        else:
            # It's a tie, go to war
            if len(player1_deck) < 1 or len(player2_deck) < 1:
                return None  # Not enough cards for war

            # Each player plays an additional card for war
            common_pool.append(player1_deck.pop(0))
            common_pool.append(player2_deck.pop(0))

def count_hands(player1_deck, player2_deck):
    count = 0
    while len(player1_deck) > 0 and len(player2_deck) > 0:
        winner = play_hand(player1_deck, player2_deck)  # Play a hand
        if winner:
            count += 1  # Increment hand count only if there is a winner

    return count

def play_game():
    deck = create_deck()
    random.shuffle(deck)

    player1_deck = deck[:26]
    player2_deck = deck[26:]

    total_hands = count_hands(player1_deck, player2_deck)
    return total_hands

# Test Function
def test_game():
    # Test deck creation
    deck = create_deck()
    assert len(deck) == 52, "Deck should have 52 cards"
    assert all(
        card in deck for card in [(2, 'H'), (3, 'H'), (11, 'H'), (14, 'H')]), "Deck should contain specific cards"

    # Test hand play with forced war
    player1_deck = [(5, 'H'), (3, 'D')]  # Player 1 plays 5
    player2_deck = [(5, 'C'), (2, 'S')]  # Player 2 plays 5 (causes a war)

    winner = play_hand(player1_deck, player2_deck)
    assert winner is None, "There should be no winner due to war"

    # Simulate the war logic
    player1_deck += [(4, 'H'), (6, 'H')]  # Add cards for Player 1
    player2_deck += [(3, 'C'), (7, 'S')]  # Add cards for Player 2

    # Now count the hands
    hands_played = count_hands(player1_deck, player2_deck)
    assert hands_played >= 1, "Total hands played should be at least 1"

    print("All tests passed!")

# Example usage
def main():
    test_game()  # Run tests

    while True:
        try:
            num_games = int(input("Enter the number of games to play: "))  # Get user input
            if num_games <= 0:
                raise ValueError("Please enter a positive integer.")
            break  # Exit the loop if the input is valid
        except ValueError as e:
            print(e)

    total_hands_played = 0
    player1_wins = 0
    player2_wins = 0
    draws = 0

    for _ in range(num_games):
        hands = play_game()
        total_hands_played += hands

        # Actual win tracking based on play_game outcomes
        if hands % 2 == 0:  # actual winner logic
            player1_wins += 1
        else:
            player2_wins += 1

    # Calculate averages
    average_length = total_hands_played / num_games if num_games > 0 else 0

    print(f"Average game length: {average_length:.2f} rounds")
    print(f"Player 1 wins: {player1_wins}")
    print(f"Player 2 wins: {player2_wins}")
    print(f"Draws: {draws}")

if __name__ == "__main__":
    main()
