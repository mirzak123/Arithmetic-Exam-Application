import random


def simple_operations():
    score = 0
    for _ in range(5):
        num_1, num_2 = random.choices(range(2, 10), k=2)
        operation = random.choice(['+', '-', '*'])
        if operation == '+':
            result = num_1 + num_2
        elif operation == '-':
            result = num_1 - num_2
        else:
            result = num_1 * num_2

        print(num_1, operation, num_2)
        while True:
            try:
                user_solution = int(input())
            except ValueError:
                print('Incorrect format.')
            else:
                break
        if user_solution == result:
            score += 1
            print('Right!')
        else:
            print('Wrong!')

    return score


def integral_squares():
    score = 0
    for _ in range(5):
        num = random.choice(range(11, 30))
        print(num)
        while True:
            try:
                user_solution = int(input())
            except ValueError:
                print('Wrong format! Try again.')
            else:
                break
        if user_solution == num ** 2:
            score += 1
            print('Right!')
        else:
            print('Wrong!')

    return score


def main():
    while True:
        print('Which level do you want? Enter a number:')
        print('1 - simple operations with numbers 2-9')
        print('2 - integral squares of 11-29')
        level = input()
        if level in ('1', '2'):
            break
        print('Incorrect format.')

    if level == '1':
        lvl_msg = "(simple operations with numbers 2-9)"
        score = simple_operations()
    else:
        lvl_msg = "(integral squares of 11-29)"
        score = integral_squares()

    print(f'Your mark is {score}/5.', end=' ')
    print('Would you like to save the result? Enter yes or no.')
    save_choice = input().lower()

    if save_choice in ('yes', 'y'):
        print('What is your name?')
        user_name = input()
        with open('results.txt', 'a') as results_file:
            print(f"{user_name}: {score}/5 in level {level} {lvl_msg}", file=results_file, flush=True)
            print('The results are saved in "results.txt".')


if __name__ == '__main__':
    main()
