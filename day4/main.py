# Open file
# def pair(line):
    

def main():
    with open("adventofcode2022/day4/data.txt", "r") as i:
        lines = i.read().split("\n")

    for line in lines:
        line = tuple(line.split(","))
        print(type(line))
    


if __name__ == "__main__":
    main()