import codecs


def make_repeater(n):
    return lambda s: s * n


twice = make_repeater(2)
print(twice)
print(twice('word'))
print(twice(5))

file = open('精绝古城.txt', encoding="utf8")
output = open('output.txt', 'x', encoding="utf8")
while 1:
    line = file.readline()
    output.writelines(line)
    print(line)
    if not line:
        break
