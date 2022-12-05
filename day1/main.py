with open("day1\data.txt") as i:
    lines = i.readlines()

elfs = []
calories = 0

for line in lines:
    if line != "\n":
        calories = calories + int(line)
    else:
        elfs.append(calories)
        calories = 0

print(max(elfs))