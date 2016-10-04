
import random

ratings = {}

def ratings_sort():
    restaurant_info = open("scores.txt")
    for line in restaurant_info:
        clean_line = line.rstrip()
        split_line = clean_line.split(":")
        restaurant = split_line[0]
        score = split_line[1]
        ratings[restaurant] = score

    alphabetized = sorted(ratings)

    for key in alphabetized:
        print key + " is rated at " + ratings[key] + "."

    restaurant_info.close()

    return ratings   

def user_score_restaurants():
    restaurant_info = open("scores.txt", "ab+")
    name = raw_input("What is the name of the restaurant you want to add?")
    score = int(raw_input("""What is the score you would like to give to the
restaurant?"""))
    specific_info = "\n" + name + " : " + str(score)
    restaurant_info.write(specific_info)
    restaurant_info.close()

# def update_random():
#     restaurant_info = open("scores.txt")
#     restaurants = []
#     for line in restaurant_info:
#         restaurants.append(line)
#     restaurant_choice = random.choice(restaurants)
#     split_choice = restaurant_choice.split(":")
#     print "Your random restaurants is: " , split_choice[0], "which has a score of", split_choice[1]
#     restaurant_info.close()
#     restaurant_info = open("scores.txt", "w")
#     for line in restaurant_info:
#         if line == restaurant_choice:
#             restaurant_info.



while True:
    user_input = int(raw_input("""Please enter 1 to view all ratings, 
2 to add a new restaurant rating, 3 to randomly update a restaurant rating,
or 4 to quit.
"""))
    if user_input == 4:
        break
    elif user_input == 1:
        ratings_sort()
    elif user_input == 2:
        user_score_restaurants()
    elif user_input == 3:
        update_random()
    else:
        print "Please enter valid input"