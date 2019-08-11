import statistics

# mean() : データの算術平均。
# harmonic_mean() : データの調和平均。
# median() : データの中央値。
# median_low() : データの low median。
# median_high() : データの high median。
# median_grouped() : grouped data の中央値、すなわち50パーセンタイル。
# mode() : 離散データの最頻値。

num = [1, 5, 6, 8, 4, 6, 8, 9]

print("mean = " + str(statistics.mean(num)))
print("median_grouped = " + str(statistics.median_grouped(num)))
print("median_high = " + str(statistics.median_high(num)))
