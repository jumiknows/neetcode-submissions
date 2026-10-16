class Solution:

  def isValid(self, s: str) -> bool:
    # This is your empty pocket (stack)
    pocket = []

    # These are the pairs where the lock points to the key
    matching_pairs = {")": "(", "}": "{", "]": "["}

    for character in s:
      # If it's a closing bracket (a lock)
      if character in matching_pairs:
        # Pull the last key out of your pocket. 
        # If your pocket is empty, hand it a fake dummy key ("#") instead.
        last_key = pocket.pop() if pocket else "#"

        # Check if the key matches the lock
        if matching_pairs[character] != last_key:
          return False  # It doesn't fit! Game over.
      else:
        # If it's an opening bracket (a key), drop it into your pocket
        pocket.append(character)

    # If your pocket is completely empty at the end, it's a success!
    return not pocket