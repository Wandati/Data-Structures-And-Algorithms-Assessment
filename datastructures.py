# Solution1
# stacks
def is_balanced(expression):
    stack = []
    for char in expression:
        if char in ['(','{','[']:
            stack.append(char)
        else:
            if not stack:
                return False
            top_stack = stack.pop()
            if (char == '}' and top_stack != "{") or (char == ')' and top_stack != "(") or (char == ']' and top_stack != "["):
                
                return False
    if stack:
        return False
    
    return True

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1)) # Output: True
print(is_balanced(expression2)) # Output: False
# Solution 2
# Sequences (Lists/Tuples)
def remove_duplicates(sequence):
    new_set = set()
    sequence_list = []
    for item in sequence:
        if item not in new_set:
            sequence_list.append(item)
            new_set.add(item)
    return sequence_list
   
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result) # Output: [2, 3, 4, 5, 6, 7]

# Solution 3
# Dictionaries:
def word_frequency(sentence):
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = "This is a test sentence This sentence is a test"
result = word_frequency(sentence)
print(result)
