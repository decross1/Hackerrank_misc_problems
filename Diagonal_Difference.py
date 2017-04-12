## Hackerrank: Diagonal Difference
n = int(raw_input().strip())
a = []
left_diag = []
right_diag = []

for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    a.append(a_temp)


def first_diag(a):
    line_start = 0
    a_length = len(a)
    position_start = 0
    for x, c in enumerate(a):
        if x <= line_start:
            if position_start < a_length:
                left_diag.append(c[position_start])
                position_start += 1
            else:
                position_start += 1
            line_start += 1


def second_diag(a):
    line_start = 0
    a_length = len(a)
    position_start = (len(a) - 1)
    for x, c in enumerate(a):
        if x <= line_start:
            if position_start < a_length and position_start >= 0:
                right_diag.append(c[position_start])
                position_start -= 1
            else:
                position_start -= 1
            line_start += 1


first_diag(a)
second_diag(a)
print(abs(sum(left_diag) - sum(right_diag)))
