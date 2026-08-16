from copy import copy, deepcopy


class MarvelCharacter:
    universe = "Marvel Universe"

    def __init__(self, name, age):
        if age < 0:
            raise ValueError(f"age must be non-negative, got {age}")
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is a {self.age}-year-old character of the {self.universe}."

    def __str__(self):
        return self.describe()


class Avenger(MarvelCharacter):
    team = "Avengers"

    def __init__(self, name, age, power_level):
        super().__init__(name, age)
        if power_level <= 0:
            raise ValueError(f"power_level must be positive, got {power_level}")
        self.power_level = power_level
        self.powers = ["Combat Training", "Enhanced Reflexes"]

    def use_signature_move(self):
        return f"{self.name} unleashes their signature move as a member of the {self.team}!"

    def describe(self):
        base_description = super().describe()
        return f"{base_description} They fight for the {self.team} with a power level of {self.power_level}."


def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    avenger1 = Avenger("Iron Man", 45, 9)
    avenger2 = Avenger("Captain America", 105, 8)

    print(f"Class variable via class:  Avenger.team = {Avenger.team}")
    print(f"Class variable via object: avenger1.team = {avenger1.team}")

    avenger1.mentor = "Nick Fury"

    print(f"\navenger1.__dict__ (has extra 'mentor' attribute): {avenger1.__dict__}")
    print(f"avenger2.__dict__ (no 'mentor' attribute):         {avenger2.__dict__}")

    print(f"\nAvenger class namespace (own attributes only): {list(Avenger.__dict__.keys())}")


def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = Avenger("Thor", 1500, 10)
    print(f"Original before mutation: {original.powers}")

    # shallow copy: new Avenger, but powers still points at the same list
    shallow = copy(original)
    # deep copy: powers is an independent list too
    deep = deepcopy(original)

    original.powers.append("Odin Force")

    print("\nAfter appending 'Odin Force' to original.powers:")
    print(f"original.powers: {original.powers}  (mutated)")
    print(f"shallow.powers:  {shallow.powers}  (changed too - shares the same list object as original)")
    print(f"deep.powers:     {deep.powers}  (unchanged - has its own independent list)")


## Edge Case: invalid input to a constructor, handled instead of crashing

def demonstrate_error_handling():
    print("\n=== Error Handling Demonstration ===")
    try:
        Avenger("Malformed", 100, -10)
    except ValueError as error:
        print(f"Could not create avenger: {error}")

    try:
        MarvelCharacter("Malformed", -5)
    except ValueError as error:
        print(f"Could not create character: {error}")


## Customization: student-created extension beyond the TODOs

def demonstrate_roster_extension():
    print("\n=== Student Extension: Avengers Roster ===")

    roster = [
        MarvelCharacter("Doctor Doom", 40),
        Avenger("Iron Man", 45, 9),
        Avenger("Captain America", 105, 8),
        Avenger("Thor", 1500, 10),
    ]

    total_age = sum(character.age for character in roster)
    print(f"Roster size: {len(roster)}")
    for character in roster:
        print(f"  - {character.describe()}")
    print(f"Combined age of everyone on the roster: {total_age} years")


def main():
    print("=== Unit 1 OOP Assignment ===")

    parent_character = MarvelCharacter("Nick Fury", 60)
    print("\nParent object:")
    print(parent_character.describe())

    child_character = Avenger("Iron Man", 45, 9)
    print("\nChild object (inherits describe(), overrides it, and adds use_signature_move()):")
    print(child_character.describe())
    print(child_character.use_signature_move())

    demonstrate_namespaces()
    demonstrate_copying()
    demonstrate_error_handling()
    demonstrate_roster_extension()


if __name__ == "__main__":
    main()
