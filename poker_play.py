import poker_cards
players_cards = {}
comunity_cards = []
players = ["Dealer", "Player_1", "Player_2", "Player_3", "Player_4"]
Hand = []

poker_cards.shuffle_card()
for player in players:
    players_cards[player] = [poker_cards.draw_card(), poker_cards.draw_card()]
comunity_cards = [poker_cards.draw_comunity_cards(), poker_cards.draw_comunity_cards(), poker_cards.draw_comunity_cards(), poker_cards.draw_comunity_cards(), poker_cards.draw_comunity_cards()]
poker_cards.check_players_hands(players_cards, comunity_cards)