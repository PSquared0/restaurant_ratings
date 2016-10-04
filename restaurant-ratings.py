

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


while True:
    user_input = int(raw_input("""Please enter 1 to view all ratings, 
2 to add a new restaurant rating, or 3 to quit.
"""))
    if user_input == 3:
        break
    elif user_input == 1:
        ratings_sort()
    elif user_input == 2:
        user_score_restaurants()
    else:
        print "Please enter valid input"