# def count_characters(string):
    # count_dict = {}
    # for c in string:
    #     if c in count_dict:
    #         count_dict[c] += 1
    #     else:
    #         count_dict[c] = 1
    # print(count_dict)
# from collections import defaultdict
# def count_characters(string):
#     count_dict = defaultdict(int)
#     for c in string:
#         count_dict[c] += 1
#     print(count_dict)

from collections import Counter
def count_characters(string):
    print(Counter(string))

if __name__ == "__main__":
    count_characters("Dynasty")
