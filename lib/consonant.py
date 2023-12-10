def highest_value_consonant(s):
    # Function to calculate the value of a consonant
    consonant_value = lambda consonant: ord(consonant) - ord('a') + 1

    # List comprehension to get the values of consonants
    consonant_values = [consonant_value(char) for char in s if char not in 'aeiou']

    # Check if the list is not empty before finding the maximum
    return max(consonant_values, default=0)

input_string = "youngren"
result = highest_value_consonant(input_string)
print(result) 