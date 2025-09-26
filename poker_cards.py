import random
from collections import Counter
suits = ["Heart", "Diamond", "Spade", "Club"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
deck = [{"suit": suit, "number": number} for suit in suits for number in numbers]
players_cards = {}
comunity_cards = []
players = ["Dealer", "Player_1", "Player_2", "Player_3", "Player_4"]



def shuffle_card():
    random.shuffle(deck)

def draw_card():
    card = deck.pop()
    return(card)

def draw_comunity_cards():
    card = draw_card()
    comunity_cards.append(card)
    return card

def check_hand_number(player_name):
    current_hand = players_cards[player_name] + comunity_cards
    numbers_in_hand = [card["number"] for card in current_hand]
    return numbers_in_hand

def check_hand_suit(player_name):
    current_hand = players_cards[player_name] + comunity_cards
    suits_in_hand = [card["suit"] for card in current_hand]
    return suits_in_hand

def check_one_pair(hand_numbers):
    counts = Counter(hand_numbers)
    for count in counts.values():
        if count == 2:
            return True
    return False

def check_two_pair(hand_numbers):
    counts = Counter(hand_numbers)
    pair_count = 0
    for count in counts.values():
        if count == 2:
            pair_count += 1
    if pair_count == 2:
        return True
    return False

def check_three_card(hand_numbers):
    counts = Counter(hand_numbers)
    for count in counts.values():
        if count == 3:
            return True
    return False

def check_straight(hand_numbers):
    unique_numbers = sorted(list(set(hand_numbers)))
    for i in range(len(unique_numbers) - 4):
        if unique_numbers[i] + 1 == unique_numbers[i+1] and unique_numbers[i+1] + 1 == unique_numbers[i+2] and unique_numbers[i+2] + 1 == unique_numbers[i+3] and unique_numbers[i+3] + 1 == unique_numbers[i+4]:
            return True
        if 1 in unique_numbers and 10 in unique_numbers and 11 in unique_numbers and 12 in unique_numbers and 13 in unique_numbers:
            return True
    return False

def check_flush(hand_suits):
    counts = Counter(hand_suits)
    for count in counts.values():
        if count >= 5:
            return True
    return False

def check_full_house(hand_numbers):
    counts = Counter(hand_numbers)
    pair_count_1 = 0
    pair_count_2 = 0
    for count in counts.values():
        if count == 2:
            pair_count_1 += 1
        elif count == 3:
            pair_count_2 += 1
    if pair_count_1 == 1 and pair_count_2 == 1:
        return True
    return False

def check_four_card(hand_numbers):
    counts = Counter(hand_numbers)
    for count in counts.values():
        if count == 4:
            return True
    return False

def check_straight_flush(hand_numbers, hand_suits):
    if check_straight(hand_numbers) and check_flush(hand_suits):
        return True
    return False

def check_royal_straight_flush(hand_numbers, hand_suits):
    if check_straight_flush(hand_numbers, hand_suits):
       unique_numbers = set(hand_numbers)
       royal_numbers = {1, 10, 11, 12, 13}
       if unique_numbers.issuperset(royal_numbers):
                return True
    return False

def check_players_hands(players_cards, comunity_cards):
    for player_name in players:
        current_hand = players_cards[player_name] + comunity_cards
        numbers = [card["number"] for card in current_hand]
        suits = [card["suit"] for card in current_hand]
        if check_royal_straight_flush(numbers,suits):
            print(f"{player_name} have ROYAL STRAIGHT FLUSH")
        elif check_straight_flush(numbers,suits):
            print(f"{player_name} have straight flush")
        elif check_four_card(numbers):
            print(f"{player_name} have four card")
        elif check_full_house(numbers):
            print(f"{player_name} have full house")
        elif check_flush(suits):
            print(f"{player_name} have flush")
        elif check_straight(numbers):
            print(f"{player_name} have straight")
        elif check_three_card(numbers):
            print(f"{player_name} have three card")
        elif check_two_pair(numbers):
            print(f"{player_name} have two pair")
        elif check_one_pair(numbers):
            print(f"{player_name} have one pair")
        else:
            print(f"{player_name} have high card")

def get_player_card_rank(numbers, suits):
        if check_royal_straight_flush(numbers,suits):
            return 9
        elif check_straight_flush(numbers,suits):
            return 8
        elif check_four_card(numbers):
            return 7
        elif check_full_house(numbers):
            return 6
        elif check_flush(suits):
            return 5
        elif check_straight(numbers):
            return 4
        elif check_three_card(numbers):
            return 3
        elif check_two_pair(numbers):
            return 2
        elif check_one_pair(numbers):
            return 1
        else:
            return 0
        
def determine_winner(players_cards, comunity_cards):
    player_results = []
    for player_name in players:
        numbers = [card["number"] for card in players_cards[player_name] + comunity_cards]
        suits = [card["suit"] for card in players_cards[player_name] + comunity_cards]
        rank = get_player_card_rank(numbers, suits)
        player_results.append({"name": player_name, "rank": rank})
    sorted_results = sorted(player_results, key=lambda x: x['rank'], reverse=True)
    winner = sorted_results[0]
    print(f"Winner is {winner['name']}!")