import random
from BlackJackArt import logo

def deal_Card():
    """Returns a random card from the list of cards"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10, 11]
    card = random.choice(cards)
    return card
def calculate_Score(list):
    """Returns the total score of list."""
    if sum(list) == 21 and len(list)==2:
        return 0
    if 11 in list and sum(list) >21:
            list.remove(11)
            list.append(1)
    return sum(list)

def compare(uScore,cScore):
    """Compare user Score and computer Score and returns if it's a draw or who wins"""
    if uScore >21 and cScore >21:
        return "You went over 21 you Lose!!"
    if uScore == cScore:
        return "Draw!!"
    elif cScore == 0:
        return "You Lose!!.Dealer wins with a BlackJack"
    elif uScore ==0:
        return "You win with a BlackJack"
    elif uScore >21:
        return "You Lose!! You went over 21."
    elif  cScore > 21:
        return "You win Dealer went over 21."
    elif uScore > cScore:
        return "You win!!"
    else:
        return "You Lose!!"

def playBlackJack():
    print(logo)
    users_cards = []
    computer_cards = []
    is_gameOver = False
    for _ in range(2):
        users_cards.append(deal_Card())
        computer_cards.append(deal_Card())

    while not is_gameOver:
        user_score = calculate_Score(users_cards)
        comp_score = calculate_Score(computer_cards)
        print(f"Your hand {users_cards}. and your score {user_score}")
        print(f"Dealer first card {computer_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_gameOver = True
        else:
            user_deal = input("Type 'y' to draw another card or type 'n' to pass : ").lower()
            if user_deal == 'y':
                users_cards.append(deal_Card())
            else:
                is_gameOver = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_Card())
        comp_score = calculate_Score(computer_cards)

    print(f"Your final hand {users_cards}, final score : {user_score}")
    print(f"Dealer's final hand {computer_cards}, final score : {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of BlackJack press 'y' to play : ").lower() == 'y':
    playBlackJack()

