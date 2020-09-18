import random

score = 0

rcp15 = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge',
         'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
rcp5 = ['paper', 'rock', 'lizard', 'spock', 'scissors']


def check_win_15(choice, ai_choice):
    """Win condition for 15 element rps game varian"""
    global rcp15
    idx = rcp15.index(choice)
    # placing index in the center of temp list win if on the right side, lose
    # if on the left side
    sort = rcp15[idx - 7:] + rcp15[:idx - 7]
    if ai_choice in sort[:7]:
        return get_results(ai_choice)
    if ai_choice == choice:
        return get_results(ai_choice, 'draw')
    return get_results(ai_choice, 'win')


def check_win_5(choice, ai_choice):
    """Win condition for 5 element rps game variant"""
    global rcp5
    idx = rcp5.index(choice)
    sort = rcp5[idx - 2:] + rcp5[:idx - 2]
    win = sort[:1] + sort[3:4]
    if ai_choice in win:
        return get_results(ai_choice, 'win')
    if ai_choice == choice:
        return get_results(ai_choice, 'draw')
    return get_results(ai_choice)


def check_win(p_c, a_c):
    """Win condition for normal game variant"""
    choices = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    if p_c == choices[a_c]:
        return get_results(a_c, 'win')
    if p_c == a_c:
        return get_results(a_c, 'draw')
    return get_results(a_c)


def get_score(nick):
    """Gets users rating from file and set score if there is no set score to 0"""
    with open('rating.txt', 'r') as rating:
        for line in rating:
            user, score = line.strip().split()
            if user == nick:
                return int(score)
    return 0


def ai_choice(choices):
    return random.choice(choices)


def get_results(a_c, result=""):
    global score
    if result == "win":
        score += 100
        return f'Well done. The computer chose {a_c} and failed'
    if result == "draw":
        score += 50
        return f'There is a draw ({a_c})'
    return f'Sorry, but the computer chose {a_c}'


def main():
    global score, rcp5, rcp15
    choices = ['rock', 'scissors', 'paper']
    inp = input("Enter your name: ")
    score = get_score(inp)
    print(f"Hello, {inp}")
    game = len(input().split(','))
    print("Okay, let's start")
    while True:
        inp = input()
        if inp == "!rating":
            print(f'Your rating: {score}')
            continue
        if inp == "!exit":
            print('Bye!')
            break
        if game == 1:
            if inp in choices:
                print(check_win(inp, ai_choice(choices)))
            else:
                print("Invalid input")
        elif game == 5:
            if inp in rcp5:
                print(check_win_5(inp, ai_choice(rcp5)))
            else:
                print("Invalid input")
        elif game == 15:
            if inp in rcp15:
                print(check_win_15(inp, ai_choice(rcp15)))
            else:
                print("Invalid input")


if __name__ == "__main__":
    main()