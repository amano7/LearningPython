import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as f:
    csv_w = csv.writer(f, delimiter=",")
    # for movie in movies:
    csv_w.writerows(movies)
