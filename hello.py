# star = 1
# while star < 5:
#     print("*" * 4)
#     star += 1
#
# print(int(98.6))
#
#
# numbers = [20,5,25,14,30,10,15,40,35,50]
# max_num = 0
# for number in numbers:
#     if number > max_num:
#         max_num = number
# print(max_num)
# print(max(numbers))
#
# sum = 0
# count = 0
# for number in numbers:
#     sum += number
#     count += 1
#     average = sum / count
# print(sum)
# print(count)
# print(average)
#
# small_number = None
# for number in numbers:
#     if small_number is None:
#         small_number = number
#     elif number < small_number:
#         small_number = number
# print(small_number)

# hours = float(input("Enter Hours: "))
# rate = 10.50
# if hours > 40:
#     pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
# else:
#     pay = hours * rate
# print(pay)
# print(2**0.5, 3**0.5, 4**0.5, 5**0.5, 6**0.5, 7**0.5, 8**0.5, 9**0.5, 10**0.5)

# find prime number from range 1 - 100
# numbers = list(range(1, 101))
# prime_numbers = []
# for number in numbers:
#     if number > 1:  # prime numbers are greater than 1
#         is_prime = True
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_numbers.append(number)
# print(prime_numbers)
import random
def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

def check_winner(player, computer):
    print(f"You chose: {player}, Computer chose: {computer}")
    if player == computer:
        return "It's a tie!"
    if palyer != computer:
    return [player, computer]

