<<<<<<< HEAD
# Class for each elf, with start and end of area range
class Elf:
    def __init__(self, line: tuple):
        self.start = int(line[0])
        self.end = int(line[1])
        self.area_range = range(self.start, self.end + 1)
 
# If elf1 range is fully contained in elf2 or vice versa, returns True
def is_fully_contained(elf1: range, elf2: range) -> bool:
    # range.__contains__(x) checks if single value x is in range, but not if range is in range, so i need to iterate over the range of elf1 and check if each value is in elf2.range
    if all(x in elf2.area_range for x in elf1.area_range) or all(x in elf1.area_range for x in elf2.area_range):
        return True
    else:
        return False

# If elf1 and elf2 overlap, returns Trueq
def overlap(elf1: range, elf2: range) -> bool:
    if any(x in elf2.area_range for x in elf1.area_range) or any(x in elf1.area_range for x in elf2.area_range):
        return True
    else:
        return False


=======
>>>>>>> 5964624 (nie pamietam juz co to bylo)
def main():
    with open("day4/data.txt", "r") as i:
        lines = i.read().split("\n")

    # Counters
    fullly_contained_output  = 0
    overlap_output = 0

    for line in lines:
        line = tuple(line.split(","))
        elf1 = Elf(line[0].split("-"))
        elf2 = Elf(line[1].split("-"))
        # Check if elf1 is fully contained in elf2 or vice versa
        if is_fully_contained(elf1, elf2):
            fullly_contained_output += 1
        # Check if elf1 and elf2 overlap
        if overlap(elf1, elf2):
            overlap_output += 1

    print(f"Part one: {fullly_contained_output}")
    print(f"Part two: {overlap_output}")

        

if __name__ == "__main__":
    main()