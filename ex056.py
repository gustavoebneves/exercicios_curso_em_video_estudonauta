s = 0
ct = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        ct += 1
        s += i
print('{} números foram somados\nA soma destes {} números foi igual a: {}'.format(ct, ct, s))
