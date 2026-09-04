import math


def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def demonstrate_small_dataset():
    print("\n=== SMALL DATASET TEST ===")
    liked_songs = ["Anti-Hero", "As It Was", "Blinding Lights", "Circles",
                   "Flowers", "Levitating", "Peaches", "Watermelon Sugar"]
    print(f"Liked Songs (sorted alphabetically): {liked_songs}")

    print(f"Linear search for 'Flowers': index {linear_search(liked_songs, 'Flowers')}")
    print(f"Binary search for 'Flowers': index {binary_search(liked_songs, 'Flowers')}")

    print(f"Linear search for 'Bad Blood' (not in list): index {linear_search(liked_songs, 'Bad Blood')}")
    print(f"Binary search for 'Bad Blood' (not in list): index {binary_search(liked_songs, 'Bad Blood')}")


def demonstrate_large_dataset():
    print("\n=== LARGE DATASET TEST ===")
    streaming_catalog = list(range(1, 100001))
    print(f"Streaming catalog size: {len(streaming_catalog)} track IDs")

    print(f"Linear search for track ID 73842: index {linear_search(streaming_catalog, 73842)}")
    print(f"Binary search for track ID 73842: index {binary_search(streaming_catalog, 73842)}")

    print(f"Linear search for track ID 100001 (not in catalog): index {linear_search(streaming_catalog, 100001)}")
    print(f"Binary search for track ID 100001 (not in catalog): index {binary_search(streaming_catalog, 100001)}")

    max_binary_steps = math.ceil(math.log2(len(streaming_catalog)))
    print(f"Worst case: linear search may need up to {len(streaming_catalog)} comparisons; "
          f"binary search never needs more than {max_binary_steps}.")


def demonstrate_edge_cases():
    print("\n=== EDGE CASE TESTS ===")

    print(f"Linear search on an empty catalog: {linear_search([], 'Flowers')}")
    print(f"Binary search on an empty catalog: {binary_search([], 'Flowers')}")

    single_song = ["Flowers"]
    print(f"Searching a single-song catalog for 'Flowers': "
          f"linear={linear_search(single_song, 'Flowers')}, binary={binary_search(single_song, 'Flowers')}")
    print(f"Searching a single-song catalog for 'Anti-Hero' (missing): "
          f"linear={linear_search(single_song, 'Anti-Hero')}, binary={binary_search(single_song, 'Anti-Hero')}")

    liked_songs = ["Anti-Hero", "As It Was", "Blinding Lights", "Circles",
                   "Flowers", "Levitating", "Peaches", "Watermelon Sugar"]
    print(f"Searching for the first song in the list ('Anti-Hero'): "
          f"linear={linear_search(liked_songs, 'Anti-Hero')}, binary={binary_search(liked_songs, 'Anti-Hero')}")
    print(f"Searching for the last song in the list ('Watermelon Sugar'): "
          f"linear={linear_search(liked_songs, 'Watermelon Sugar')}, binary={binary_search(liked_songs, 'Watermelon Sugar')}")


def demonstrate_real_world_scenario():
    print("\n=== REAL-WORLD SCENARIO: RECENTLY PLAYED ===")
    recently_played = ["Watermelon Sugar", "Anti-Hero", "Flowers", "As It Was", "Peaches"]
    print(f"Recently Played (kept in play order, not sorted): {recently_played}")

    linear_result = linear_search(recently_played, "Anti-Hero")
    binary_result = binary_search(recently_played, "Anti-Hero")
    print(f"Linear search for 'Anti-Hero': index {linear_result} (correct)")
    print(f"Binary search for 'Anti-Hero': index {binary_result} (WRONG - 'Anti-Hero' is really at index {linear_result})")


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    demonstrate_small_dataset()
    demonstrate_large_dataset()
    demonstrate_edge_cases()
    demonstrate_real_world_scenario()


if __name__ == "__main__":
    main()
