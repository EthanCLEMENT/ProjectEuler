import inflect
p = inflect.engine()


def count_digits(a, b):
    total_count = 0
    for i in range(a, b + 1):
        total_count += digit_to_word(i)
    return total_count


def digit_to_word(j):
    word = list(p.number_to_words(j))
    count = 0
    for k in word:
        if k not in [',', '-', ' ']:
            count += 1
    return count


sum1 = count_digits(1, 1000)
print(sum1)
