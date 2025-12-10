songs = []
genres = ()
genre_count = {}

a = 0

print("Welcome to your Song library!\n")

while a < 5:
    a += 1
    song_input=input(f"Enter Song {a}: ")


    if song_input != "" :
     genre_input=input(f"What is the genre of {song_input}: ")
     songs.append((song_input,genre_input))

for song_input, genres in songs:
   if genres in genre_count:
      genre_count[genres] +=1
   else:
      genre_count[genres] = 1
      

print("Your Music Library:\n")
for song_input, genres in songs:
    print(f"{song_input.capitalize()}({genres.capitalize()})\n")

most_popular_genre = max(genre_count, key=genre_count.get)

print("Your Genre Statistics:\n")
for genres, count in genre_count.items():
   print(f"{genres.capitalize()}:{count} songs")
print(f"Most popular genre: {most_popular_genre.capitalize()}")







#Excercise 2

student_records = []
stats = {}
scores = []
name = input

for a in range(1,7):
   name = input(f"Student {a} nane: ")
   score = int(input(f"Stunde {a} score: "))
   student_records.append((name, score))
   print()

for name, score in student_records:
 scores.append(score)

stats['highest_grade'] = max(scores)
stats['lowest_grade'] = min(scores)
stats['average_grade'] = sum(scores) / len(scores)

unique_scores = set(scores)

grade_distribution = {}
for score in scores:
    if score in grade_distribution:
        grade_distribution[score] += 1
    else:
        grade_distribution[score] = 1


print("===Student Records===")
print(student_records)

print("\n")

print("===Class Statistics===")
print(f"Highest Score: {stats['highest_grade']}")
print(f"Lowest Score: {stats['lowest_grade']}")
print(f"Average Score: {stats['average_grade']}")

print("\n")

print("===Unique Scores===")
print(unique_scores)
print(f"Total amount of unique scores: {len(unique_scores)}")

print("\n")

print("===Grade Distribution===")

scores = sorted(grade_distribution.keys(), reverse=True)

for score in scores:
    count = grade_distribution[score]

    if count == 1:
        plural = "student"
    else:
        plural = "students"

    print("Score {}: {} {}".format(score, count, plural))



#Excercise 3

expense_records = ()
category_totals = {}
unique_categories = []

expense_records.append((category, amount, date))

expenses = int(input("How many expenses do you have?: "))

for i in range(1, expenses + 1):
   print(f"\nExpense {i}:")
   
   category = input("Enter category: ")
   amount = input("Enter amount: ")
   date = input("Enter date (DD-MM-YYYY)")

print(f"\nAll expenses : {expense_records} ")
