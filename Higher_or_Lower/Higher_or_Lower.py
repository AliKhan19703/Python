import game_data_day
import art_day
import random



def get_random_account():
    """Get data from random account"""
    followers = 0
    data = game_data_day.data
    rand_Account = random.choice(data)
    followers += rand_Account["follower_count"]
    return rand_Account


def display_data(account_A, account_B):
    print(f"Compare A : {account_A['name']}, a {account_A['description']}, from {account_A['country']}")
    print(art_day.vs)
    print(f"Against B : {account_B['name']},a {account_B['description']}, from {account_B['country']}")


def compare(a, b):
    if a > b:
        return "a"
    else:
        return "b"


def play_Game():
    score = 0
    flag = True
    print(art_day.logo)
    A = get_random_account()
    B = get_random_account()
    while (flag):
        followers_A = A["follower_count"]
        followers_B = B["follower_count"]
        more_followers = compare(followers_A, followers_B)
        display_data(A, B)
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if (user_guess == more_followers):
            score += 1
            print(f"You are right! current score:{score} ")
            if (more_followers == "a"):
                B = get_random_account()
            else:
                A = B
                B = get_random_account()

        else:
            print("You are wrong")
            flag = False


play_Game()