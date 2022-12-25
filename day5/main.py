import re

def matrix_to_lists(matrix):
     # Transpose the matrix
    matrix = matrix.split("\n")
    matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    # I only need rows 2, 6, 10, 14, and so on, so i need to remove the rest
    matrix = [row for row in matrix if (matrix.index(row) +1) % 4 == 2]
    # Now reverse the matrix
    matrix = [row[::-1] for row in matrix]
    # Delete elements with just the space character
    matrix = [[element for element in row if element != ' '] for row in matrix]

    return matrix

def move_crates(procedure: str, stack_one: list) -> list:
    # Convert procedure to a list of integers
    procedure = re.findall(r'\d+', procedure)
    procedure = [int(x) for x in procedure]
    # We must iterete over the second element of the procedures, which is the number of crates to move, and move them one by one, stacking them on top of each other
    for i in range(procedure[0]):
        # Move the last item from stack[procedure[1]] to stack[procedure[2]]
        stack_one[procedure[2] - 1].append(stack_one[procedure[1]- 1].pop())
    
    return stack_one

def move_multiple_crates(procedure: str, stack: list) -> list:
    # Convert procedure to a list of integers
    procedure = re.findall(r'\d+', procedure)
    procedure = [int(x) for x in procedure]
    # Doklej do kolumny ze stack 
    stack[procedure[2] - 1].extend(stack[procedure[1]- 1][-procedure[0]:])
    # Usun z kolumny ze stack
    stack[procedure[1] - 1] = stack[procedure[1] - 1][:-procedure[0]]
    
    return stack

def main():
    with open("day5/data.txt", "r") as i:
        input = i.read()

    # Divide input into stacks and procedures:
    stack, procedures = input.split("\n\n")

    # Stack is just a matrix that looks funny and has a lot of junk, so we need to clean it up
    stack = matrix_to_lists(stack)
   
    # Procedures is a list of procedures, so i need to split it by newlines
    procedures = procedures.split("\n")

    # Copy
    stack_one = list(stack)
    stack_two = stack.copy()
    for procedure in procedures:
        move_crates(procedure, stack_one)

    # Print the result for part 1
    print("Part one:")
    for x in stack_one:
        print(x)


    # Part 2
    for procedure in procedures:
        move_multiple_crates(procedure, stack_two)
    
    print("\nPart two:")
    for x in stack_two:
        print(x)


if __name__ == "__main__":
    main()