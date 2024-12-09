def is_valid_sequence(numbers):
    diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers) - 1)]
    all_increasing = all(diff > 0 for diff in diffs)
    all_decreasing = all(diff < 0 for diff in diffs)
    
    if not all_increasing and not all_decreasing:
        
        return False
    
    return all(1 <= abs(diff) <= 3 for diff in diffs)

def is_valid_with_dampener(numbers):
    #check if valid without removing any numbers
    if is_valid_sequence(numbers):
        return True
    
    #check if valid by removing one number
    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i+1:]
        if is_valid_sequence(modified_numbers):
            return True
    
    return False

def count_valid_sequences(input_text):
    count = 0
    for line in input_text.strip().split('\n'):
        numbers = [int(x) for x in line.split()]
        if is_valid_sequence(numbers):
            count += 1
    return count

def count_valid_sequences_with_dampener(input_text):
    count = 0
    for line in input_text.strip().split('\n'):
        numbers = [int(x) for x in line.split()]
        if is_valid_with_dampener(numbers):
            count += 1
    return count

# Read from file
with open('input.txt', 'r') as file:
    input_text = file.read()

result1 = count_valid_sequences(input_text)
result2 = count_valid_sequences_with_dampener(input_text)
print(f"part1: {result1}")
print(f"part2: {result2}")