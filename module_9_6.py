def all_variants(text):
    for s in range(1, len(text) + 1):
        for j in range(len(text) + 1 - s):
            yield text[j:j + s]


a = all_variants("abc")
for i in a:
    print(i)
