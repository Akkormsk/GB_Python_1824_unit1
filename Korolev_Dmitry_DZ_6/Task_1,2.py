from collections import Counter

result_list = []
# task 1
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result_list = [(line.strip().split(' ')[0], line.strip().split(' ')[5][1:], line.strip().split(' ')[6]) for line in f]

# task 2
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result_list_2 = [line.strip().split(' ')[0] for line in f]
    most_common, num_most_common = Counter(result_list_2).most_common(1)[0]
    print(most_common, num_most_common)




