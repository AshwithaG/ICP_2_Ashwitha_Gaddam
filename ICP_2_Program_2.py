from collections import Counter

with open('input.txt') as input_:
    lines = input_.read()
    list_words = (' '.join(lines.splitlines())).split()
    count_words = str(dict(Counter(list_words)))
    with open('output.txt', 'w') as output_:
        output_.write(count_words)
        
