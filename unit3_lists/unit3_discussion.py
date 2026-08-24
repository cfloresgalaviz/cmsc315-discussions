def insert_at(lst, index, value):
    if len(lst) >= 6:
        return lst
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    if index < 0 or index >= len(lst):
        return None
    return lst.pop(index)


def search_value(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def demonstrate_insertions():
    print("\n=== INSERTION TESTS ===")

    party = ["Pikachu", "Charmander", "Nidoran"]
    print(f"Starting party: {party}")

    insert_at(party, 0, "Rattata")
    print(f"After catching Rattata (inserted at the beginning, index 0): {party}")

    insert_at(party, 2, "Snorlax")
    print(f"After catching Snorlax (inserted in the middle, index 2): {party}")

    insert_at(party, len(party), "Dratini")
    print(f"After catching Dratini (inserted at the end): {party}")
    print(f"Party size: {len(party)}/6")

    return party


def demonstrate_deletions(party):
    print("\n=== DELETION TESTS ===")

    rattata_index = search_value(party, "Rattata")
    released_rattata = delete_at(party, rattata_index)
    print(f"Released '{released_rattata}' from the front of the party: {party}")

    snorlax_index = search_value(party, "Snorlax")
    released_snorlax = delete_at(party, snorlax_index)
    print(f"Released '{released_snorlax}' from the middle of the party: {party}")

    insert_at(party, len(party), "Pidgey")
    print(f"Caught a Pidgey (inserted at the end): {party}")

    released_pidgey = delete_at(party, len(party) - 1)
    print(f"Released '{released_pidgey}' from the end of the party: {party}")

    return party


def demonstrate_search(party):
    print("\n=== SEARCH TESTS ===")

    target = party[0]
    found_index = search_value(party, target)
    print(f"Checking if '{target}' is on the team (owned): found at index {found_index}")

    missing_index = search_value(party, "Mewtwo")
    print(f"Checking if 'Mewtwo' is on the team (not owned): returned {missing_index}")


def demonstrate_edge_cases():
    print("\n=== EDGE CASES ===")

    full_party = ["Pikachu", "Dratini", "Charmander", "Snorlax", "Nidoran", "Rattata"]
    insert_at(full_party, 0, "Mewtwo")
    print(f"Trying to catch a 7th Pokemon (Mewtwo) with a full party: "
          f"party unchanged at {len(full_party)}/6 -> {full_party}")

    small_party = ["Charmander"]
    invalid_release = delete_at(small_party, 5)
    print(f"Releasing with an out-of-range index (5) on a 1-Pokemon party: "
          f"returned {invalid_release}, party unchanged -> {small_party}")

    missing_search = search_value(small_party, "Dratini")
    print(f"Checking a 1-Pokemon party for one that isn't there: returned {missing_search}")

    empty_party = []
    insert_at(empty_party, 0, "Nidoran")
    print(f"Catching a first Pokemon into an empty party: {empty_party}")

    empty_party_2 = []
    empty_release = delete_at(empty_party_2, 0)
    print(f"Releasing from an empty party: returned {empty_release}, party unchanged -> {empty_party_2}")


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    party = demonstrate_insertions()
    party = demonstrate_deletions(party)
    demonstrate_search(party)
    demonstrate_edge_cases()


if __name__ == "__main__":
    main()
