# Hackerrank: Panagram
# Enter your code here. Read input from STDIN. Print output to STDOUT
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
        , 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']

a = raw_input()
db = []
for each in a:
    if each != " ":
        if str.lower(each) not in db:
            db.append(str.lower(each))
db = sorted(db)

if db == alpha:
    print'pangram'
else:
    print 'not pangram'

## Better way to write the above function
s = 'We promptly judged antique ivory buckles for the next prize'
t = set(c.lower() for c in s if c != ' ')
print("pangram" if len(t) == 26 else "not pangram")