# Check before

- Should it allow cycles? If yes, keeping track of checked nodes is mandatory.
- For each element to be removed in the list, create hash map for O(1) value checks.
- Create a hashmap for scanned nodes.

# For each element

- Keep track of the head, if it is removed, move the pointer to the next one.
- If element matches the value, link the previous to the next.
- Iteration ends either when the pointer is `None` or it hits an already scanned node. 
