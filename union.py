def find_union(list1, list2):
    return list(set(list1) | set(list2))

list1 = input("Enter first list (comma-separated): ").split(',')
list2 = input("Enter second list (comma-separated): ").split(',')

# Optionally strip whitespace and convert to int if needed
list1 = [item.strip() for item in list1]
list2 = [item.strip() for item in list2]

result = find_union(list1, list2)
print("Union:", result)