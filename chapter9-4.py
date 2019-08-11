import csv

movies = [["トップガン", "リスキービジネス", "マイノリティーレポート"], ["タイタニック", "レベナント", "インセプション"], ["トレーニングデイ", "マンオンファイア", "フライト"]]
with open("moviesJ.csv", "w", encoding="UTF-8" ) as f:
    csv_w = csv.writer(f, delimiter=",")
    # for movie in movies:
    csv_w.writerows(movies)
