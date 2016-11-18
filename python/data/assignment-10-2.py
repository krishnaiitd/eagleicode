name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts  = {}

for line in handle.readlines():
    if line.startswith("From "):
        words = line.split()
        times = words[5]
        #print times
        hour = times.split(":")[0]
        #print hour
        if hour in counts:
            counts[hour] += 1
        else:
            counts[hour] = 1

countItems = counts.items()
for key, value in sorted(countItems):
    print key, value
