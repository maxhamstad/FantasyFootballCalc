class FantasyPlayer:
    def __init__(self, name, value):
        """Constructor to initialize a fantasy football player with name and value."""
        self.name = name
        self.value = value

    def display_info(self):
        """Displays player information."""
        print(f"{self.name} - Trade Value: {self.value}")

    def compare_trade(self, other_players):
        """Compares the trade values of two lists of players."""
        total_value_self = sum(player.value for player in self)
        total_value_other = sum(player.value for player in other_players)

        if total_value_self > total_value_other:
            print(f"Your trade is more valuable! Your trade value is {total_value_self} vs {total_value_other}.")
        elif total_value_self < total_value_other:
            print(f"The other player's trade is more valuable! Trade value: {total_value_other} vs {total_value_self}.")
        else:
            print(f"Both trades have equal value! Total trade value is {total_value_self}.")

# List of players and their corresponding values
players_data = {
    "JaMarr Chase": 9999,
    "Josh Allen": 9998,
    "Jayden Daniels": 9994,
    "Lamar Jackson": 9979,
    "Justin Jefferson": 9221,
    "Malik Nabers": 8383,
    "Jahmyr Gibbs": 8310,
    "Joe Burrow": 8273,
    "Brock Bowers": 8232,
    "Jalen Hurts": 8227,
    "Bijan Robinson": 8084,
    "CeeDee Lamb": 7830,
    "Puka Nacua": 7696,
    "Amon-Ra St. Brown": 7615,
    "Brian Thomas Jr.": 7613,
    "Patrick Mahomes": 6980,
    "Justin Herbert": 6890,
    "Ashton Jeanty": 6871,
    "Nico Collins": 6823,
    "Drake Maye": 6797,
    "Caleb Williams": 6690,
    "C.J. Stroud": 6689,
    "Drake London": 6666,
    "Saquon Barkley": 6654,
    "Marvin Harrison Jr.": 6574,
    "Jaxon Smith-Njigba": 6515,
    "Bo Nix": 6501,
    "Ladd McConkey": 6501,
    "Trey McBride": 6498,
    "2025 Early 1st": 6395,
    "Jordan Love": 6390,
    "DeVon Achane": 6336,
    "A.J. Brown": 6264,
    "Garrett Wilson": 6231,
    "Breece Hall": 5980,
    "Tetairoa McMilan": 5939,
    "2026 Early 1st": 5727,
    "Bucky Irving": 5688,
    "Kyler Murray": 5643,
    "Tee Higgins": 5612,
    "Brock Purdy": 5558,
    "2027 Early 1st": 5515,
    "Rome Odunze": 5496,
    "Baker Mayfield": 5475,
    "Rashee Rice": 5462,
    "Kyren Williams": 5454,
    "Trevor Lawrence": 5436,
    "Jonathan Taylor": 5415,
    "J.J. McCarthy": 5397,
    "James Cook": 5388
}

# Create player objects and store them in a list
players = [FantasyPlayer(name, value) for name, value in players_data.items()]

# Function to display player list
def display_player_list():
    print("\nAvailable Players:")
    for index, player in enumerate(players, start=1):
        print(f"{index}. {player.name}")

# Allow user to select players for trade
def get_players_for_trade():
    trade_players = []
    while True:
        try:
            player_choice = int(input("\nEnter the numbers of the players for team A to trade (or 0 to stop): "))
            if player_choice == 0:
                break
            elif player_choice < 1 or player_choice > len(players):
                print("Invalid choice! Please select a valid player number.")
                continue
            trade_players.append(players[player_choice - 1])
        except ValueError:
            print("Please enter a valid number.")
    return trade_players

# Main program loop
def main():
    display_player_list()
    print("\nEnter 1 number at a time:")
    user_trade_players = get_players_for_trade()

    # Get players for the other person's trade side
    print("\nSelect the players team B wants to trade (enter 0 to stop selecting):")
    other_trade_players = get_players_for_trade()

    # Display the trade comparison
    print("\nComparing team A's trade vs team B's trade:")
    print("Team A trade players:")
    for player in user_trade_players:
        player.display_info()
    
    print("\nTeam B's player's:")
    for player in other_trade_players:
        player.display_info()

    # Compare the total values of the two sides
    FantasyPlayer.compare_trade(user_trade_players, other_trade_players)

if __name__ == "__main__":
    main()
