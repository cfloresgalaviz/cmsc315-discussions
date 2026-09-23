def demonstrate_insert_operations():
    print("\n=== INSERT OPERATIONS ===")
    pokedex = {}
    pokedex["Pikachu"] = {"type": "Electric", "level": 25, "hp": 60}
    pokedex["Charmander"] = {"type": "Fire", "level": 12, "hp": 39}
    pokedex["Snorlax"] = {"type": "Normal", "level": 30, "hp": 160}
    pokedex["Dratini"] = {"type": "Dragon", "level": 15, "hp": 41}
    pokedex["Nidoran"] = {"type": "Poison", "level": 10, "hp": 30}
    print(f"Pokedex: {pokedex}")
    return pokedex


def demonstrate_lookup_operations(pokedex):
    print("\n=== LOOKUP OPERATIONS ===")
    print(f"Pikachu's entry: {pokedex['Pikachu']}")
    print(f"Snorlax's entry: {pokedex['Snorlax']}")


def demonstrate_update_operations(pokedex):
    print("\n=== UPDATE OPERATIONS ===")
    print(f"Charmander's entry before training: {pokedex['Charmander']}")
    pokedex["Charmander"]["level"] = 13
    print(f"Charmander's entry after training: {pokedex['Charmander']}")


def demonstrate_delete_operations(pokedex):
    print("\n=== DELETE OPERATIONS ===")
    print(f"Pokedex before release: {pokedex}")
    del pokedex["Nidoran"]
    print(f"Pokedex after releasing Nidoran: {pokedex}")


def demonstrate_edge_cases(pokedex):
    print("\n=== EDGE CASES ===")

    print(f"Looking up a Pokemon never caught ('Mewtwo'): {pokedex.get('Mewtwo')}")

    pokedex.pop("Mewtwo", None)
    print("Releasing a Pokemon that was never caught ('Mewtwo') did not raise an error.")

    pokedex["Bulbasaur"] = {"type": "Grass", "level": 8, "hp": 45}
    print(f"'Training' a Pokemon not previously in the Pokedex actually caught it "
          f"instead: {pokedex['Bulbasaur']}")

    empty_pokedex = {}
    print(f"Looking up any Pokemon in an empty Pokedex: {empty_pokedex.get('Pikachu')}")


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    pokedex = demonstrate_insert_operations()
    demonstrate_lookup_operations(pokedex)
    demonstrate_update_operations(pokedex)
    demonstrate_delete_operations(pokedex)
    demonstrate_edge_cases(pokedex)


if __name__ == "__main__":
    main()
