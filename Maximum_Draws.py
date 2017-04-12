## Hackerrank: Maximum Draws
# Enter your code here. Read input from STDIN. Print output to STDOUT
draws = int(raw_input())

total_socks = []

while draws > 0:
    total_socks.append(raw_input())
    draws -= 1

for each in total_socks:
    print
    int(each) + 1
