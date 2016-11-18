import operator

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

sends = {}

for line in handle.readlines():
    if line.startswith("From "):
        from1 = line.split()[1]
        if from1 in sends:
            sends[from1] += 1
        else:
            sends[from1] = 1

touplesends = [(value, key) for (key, value) in sends.items()]

sender = sorted(touplesends, reverse=True)[0]
print sender[1], sender[0]