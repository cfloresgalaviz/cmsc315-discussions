# Unit 3 Discussion: List Operations

## Overview

This assignment examined insertion, deletion, and searching in Python lists, and how each operation's performance depends on where in the list it happens. I implemented a Pokemon trainer's party manager to demonstrate all three operations, including the game's own 6-Pokemon party limit as an extra edge case.

## What I Built

### Insertion; `insert_at()` and `demonstrate_insertions()` (TODO 1)

`insert_at()` first checks whether the party already has 6 Pokemon; the same limit the games enforce; and rejects the insert (returns the list unchanged) if it's full. Otherwise it uses `list.insert(index, value)` to catch a Pokemon into a given party slot. Inserting shifts every element currently at or after that index one position to the right to make room. Performance depends on where the insertion happens: inserting at the end needs no shifting and is O(1) amortized (the same cost as `append()`), while inserting at the beginning or middle is O(n), since up to n elements have to move over. `demonstrate_insertions()` starts with Pikachu, Charmander, and Nidoran, then catches Rattata at the beginning, Snorlax in the middle, and Dratini at the end, filling the party to exactly 6.

### Deletion; `delete_at()` and `demonstrate_deletions()` (TODO 2)

`delete_at()` validates the index first (`0 <= index < len(lst)`), returning `None` for anything out of range instead of letting an `IndexError` crash the program. A valid index is removed and returned with `list.pop(index)`, which shifts every remaining element after it one position to the left; the same O(n) shifting cost as insertion, just in the opposite direction. `demonstrate_deletions()` releases Rattata from the front and Snorlax from the middle, then catches a Pidgey at the end (using `insert_at()` again to show a second insertion opening up after some releases) before releasing it too from the end, printing the released Pokemon and the updated party at each step.

### Search; `search_value()` and `demonstrate_search()` (TODO 3)

`search_value()` is implemented as a linear search: a plain Python list has no built-in ordering or hash-based lookup for its values, so the only way to find one is to check elements one at a time from the front. Returns the index on a match, or `-1` if the loop finishes without finding the value; O(n) in the worst case, since checking whether a Pokemon is *not* on the team requires scanning the entire party. `demonstrate_search()` checks for a Pokemon known to be on the team and one that was never caught, showing the found index and the `-1` miss case side by side.

### Edge Cases; `demonstrate_edge_cases()` (TODO 4)

Covers five cases: trying to catch a 7th Pokemon with a full 6-member party (rejected, party unchanged; the Pokemon-specific edge case beyond what the assignment strictly requires), releasing with an out-of-range index (returns `None`, party untouched), searching a party for a Pokemon that isn't present (returns `-1`), catching a first Pokemon into an empty party, and releasing from an empty party (returns `None` instead of raising an error).

### Real-World Scenario (TODO 5)

The Pokemon party **is** the real-world scenario; catching a Pokemon into a specific slot, releasing one, and checking whether a given Pokemon is already on the team are all list operations, and the hard 6-member cap is a genuine real-world constraint baked directly into the games, giving the insertion logic an extra rule to enforce beyond plain index handling.

## Linked List vs. Array-Based List Performance

Python's built-in `list` is array-based: it stores elements in one contiguous block of memory, which makes indexed access (`lst[i]`) O(1), but inserting or deleting near the front is O(n) because every following element has to shift over. A linked list stores each element in its own node with a pointer to the next node, so inserting or deleting at a known position; especially near the front; is O(1): no shifting, just updating a couple of pointers. A linked list would outperform this array-based party list in a scenario with frequent insertions/deletions at arbitrary positions in a much larger collection (e.g., a full Pokedex of hundreds of entries being constantly reordered), at the cost of losing fast O(1) indexed access, which a linked list doesn't have (finding the nth element means walking the list one node at a time). For a fixed 6-slot party, though, the array-based list's O(1) indexed access is the better fit; the collection is small enough that occasional O(n) shifting barely matters.
