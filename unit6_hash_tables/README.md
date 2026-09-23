# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used a Python dictionary to demonstrate hash table behavior. I implemented a trainer's Pokedex, keyed by Pokemon name, to demonstrate insert, lookup, update, and delete operations, along with edge cases specific to how a dictionary handles missing keys.

## What I Built

### Insert Operations (TODO 1)

I created an empty dictionary and added five Pokemon, keyed by name, each mapping to a nested dictionary of type, level, and HP. A Python dict behaves like a hash table because it hashes each key to figure out exactly where to store its value, the same way flipping straight to a Pokemon's entry in the Pokedex is faster than reading through every entry in order.

### Lookup Operations (TODO 2)

`pokedex["Pikachu"]` and `pokedex["Snorlax"]` both hash the given name directly to its bucket, which is what makes dictionary lookup O(1) on average instead of the O(n) a list would need to find the same entry.

### Update Operations (TODO 3)

I updated Charmander's level after training. Assigning to an existing key doesn't create a second entry; the dict hashes "Charmander" to the same bucket it already occupies and overwrites the value stored there, so the number of Pokemon in the Pokedex never grows from an update.

### Delete Operations (TODO 4)

I released Nidoran with `del`, which removes the key and its value entirely, freeing that bucket for a future key to hash into.

### Edge Cases (TODO 5)

Covers four cases: looking up a Pokemon that was never caught (using `.get()`, which safely returns `None` instead of raising a `KeyError`), releasing a Pokemon that doesn't exist (`dict.pop(key, None)`, which does nothing instead of raising an error the way `del` would), "training" a Pokemon that isn't in the Pokedex yet (which doesn't raise an error either; it just catches it, since `dict[key] = value` doesn't distinguish between updating and inserting), and looking up any Pokemon in a completely empty Pokedex.

### Real-World Scenario (TODO 6)

The Pokedex **is** the real-world scenario: catching a Pokemon, looking up its entry, training it to a new level, and releasing it are all hash table operations wrapped in a mechanic every Pokemon player already understands.

## Collision Handling and Performance

Python's dict hides its collision handling from the programmer, but it still has to deal with it internally: whenever two different keys hash to the same bucket (a collision), the dict resolves it with open addressing, probing for the next available slot rather than storing a list of colliding entries. Collisions don't change the correctness of insert, lookup, update, or delete, but they do affect performance: the more collisions occur, the more probing has to happen before a value is found, degrading average-case O(1) lookups toward O(n) in the worst case. This is directly tied to load factor (how full the underlying table is); a hash table resizes itself once it gets too full specifically to keep collisions rare and lookups fast, which is why a well-designed hash table stays performant even as a Pokedex fills up with hundreds of entries.
