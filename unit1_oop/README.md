# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming (OOP) concepts in Python, including inheritance, class/instance namespaces, and shallow vs. deep object copying. I implemented it using a Marvel-themed class hierarchy: a `MarvelCharacter` parent class and an `Avenger` child class.

## What I Built

### Parent Class — `MarvelCharacter`

I defined `MarvelCharacter` as the base class every other type in the file builds on. It has a class variable (`universe = "Marvel Universe"`) shared by every instance, two instance variables (`name`, `age`) set in the constructor, and a `describe()` method that returns a formatted summary. The constructor validates that `age` is non-negative and raises `ValueError` otherwise. I also added a `__str__` method so `print()`/`str()` on a character shows the friendly `describe()` output instead of Python's default object representation.

### Child Class — `Avenger`

`Avenger` inherits from `MarvelCharacter` and extends it: a new class variable (`team = "Avengers"`), two new instance variables (`power_level`, validated to be positive, and `powers`, a mutable list of abilities), and a new method (`use_signature_move()`). Its constructor calls `super().__init__(name, age)` to reuse the parent's setup instead of duplicating it. `describe()` is overridden to extend the parent's version via `super().describe()` rather than replace it outright, appending team and power-level details.

### Namespace Demonstration — `demonstrate_namespaces()`

This function creates two `Avenger` objects (Iron Man and Captain America) and shows the difference between the class namespace and each instance's namespace. It reads `team` both through the class (`Avenger.team`) and through an instance (`avenger1.team`), then adds a `mentor` attribute to only one of the two objects. Printing `__dict__` on each object shows that the extra attribute exists only on the one it was assigned to, while `Avenger.__dict__.keys()` shows what lives in the class's own namespace, separate from either instance.

### Copy Demonstration — `demonstrate_copying()`

This function creates one `Avenger` (Thor) with a mutable `powers` list, then makes a shallow copy with `copy()` and a deep copy with `deepcopy()`. After appending a new power to the original's list, the shallow copy reflects the change (it shares the same underlying list object), while the deep copy does not (it has its own independent list). I used comments in the code to explain why.

### Edge Case — `demonstrate_error_handling()`

Since both constructors validate their input and raise `ValueError` on bad data, I added this function to actually exercise that path instead of leaving it untested: it deliberately tries to construct an `Avenger` with a negative `power_level` and a `MarvelCharacter` with a negative `age`, catches the resulting `ValueError` in each case, and prints a clear message instead of letting the program crash.

### Student Extension — `demonstrate_roster_extension()`

Beyond the required TODOs, I built a small scenario that mixes both classes: a team "roster" list containing a plain `MarvelCharacter` (Doctor Doom, a nod to the upcoming Fantastic Four/Doom movie) alongside several `Avenger` objects. It loops over the whole list and sums everyone's `age`, which only works uniformly because `age` and `describe()` are defined on the shared parent class.

### `main()`

Ties everything together: creates one `MarvelCharacter` and one `Avenger` object directly to demonstrate inheritance, then calls each of the four functions above in sequence.

## Real-World Application

The `MarvelCharacter`/`Avenger` relationship mirrors how a smart home is organized: a general "smart device" concept (power state, name) is the shared blueprint, while a specific device like a thermostat inherits that baseline and adds its own specialized behavior — the same way `Avenger` inherited `name`/`age` from `MarvelCharacter` and added `use_signature_move()`. The error-handling piece maps to a real annoyance with smart-home devices: a well-built one reports a problem and keeps the rest of the system running, while a poorly-built one lets one bad input crash everything. That's what the `try/except ValueError` blocks in `demonstrate_error_handling()` prevent.

## How to Run

```bash
python3 unit1_discussion.py
```
