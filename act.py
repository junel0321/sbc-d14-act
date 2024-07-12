input_string = input("Please enter a string: ")

patterns_input = input("Please enter patterns : ")

patterns = [pattern.strip() for pattern in patterns_input.split(',')]

occurrences = []

for pattern in patterns:
    pattern_length = len(pattern)
    
    for start_index in range(len(input_string) - pattern_length + 1):
        if input_string[start_index:start_index + pattern_length] == pattern:
            end_index = start_index + pattern_length - 1
            occurrences.append((pattern, start_index, end_index))

if occurrences:
    for pattern, start, end in occurrences:
        print(f"Pattern \"{pattern}\" found from index {start} to {end}.")
else:
    print(f"No occurrences of patterns {patterns} found in the input string.")
