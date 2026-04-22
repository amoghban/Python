# Linear Search
# Search and print if a given element is present in the list or not
# Linear search works on sorted or unsorted lists with time complexity O(n),
# as in the worst case, we may need to check every element.

def linear_search(my_list, element):
    """
    Perform linear search on the list to find the element.

    Args:
        my_list (list): The list to search in.
        element: The element to search for.

    Returns:
        bool: True if element is found, False otherwise.
    """
    for item in my_list:
        if item == element:
            return True
    return False

# Example usage

my_list = [34, 23, 45, 67, 12, 2, 1]
element = 45

present = linear_search(my_list, element)

if present:
    print(f"Element {element} is present in the list")
else:
    print(f"Element {element} not found in the given list!")
