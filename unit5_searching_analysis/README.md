# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compared linear search and binary search. I implemented a music library scenario: a small, alphabetically sorted "Liked Songs" list and a large, sorted streaming catalog for the required algorithm tests, plus an unsorted "Recently Played" list to demonstrate a real-world case where binary search cannot be trusted.

## What I Built

### Small Dataset Test; `linear_search()`, `binary_search()`, and the Liked Songs test (TODO 1)

`linear_search()` checks each element from the front of the list until it finds a match or runs out of elements, since it has no information about how the list is arranged; that's what makes it O(n). `binary_search()` instead compares the target against the list's middle element and discards half the remaining list every time, which only works because the list is sorted. I tested both against an 8-song, alphabetically sorted "Liked Songs" list, searching for a song that's on the list ("Flowers") and one that isn't ("Bad Blood"); both algorithms agreed on every result.

### Large Dataset Test; the streaming catalog comparison (TODO 2)

I built a 100,000-track streaming catalog (sequential track IDs, already sorted) and ran the same searches against it. Both algorithms still returned the correct index for an existing track ID (73842) and `-1` for a missing one (100001), but the number of comparisons each needs scales very differently: linear search's worst case grows with the size of the catalog itself (up to 100,000 comparisons), while binary search's worst case only grows with how many times the catalog can be cut in half (`ceil(log2(100000))`, 17 comparisons). That gap is why binary search becomes dramatically more efficient as a dataset grows larger, even though both algorithms are equally correct.

### Edge Cases (TODO 3)

Covers five cases: searching an empty catalog (both algorithms fall through to `-1` with no special-casing needed), a single-song catalog (correctly finds the one song and correctly reports a different song as missing), and searching the sorted Liked Songs list for the value at the very first position and the value at the very last position, the two extremes binary search's midpoint math has to land on correctly.

### Real-World Scenario: Recently Played

A "Recently Played" list is intentionally kept in play order rather than sorted, since sorting it would destroy the information it's meant to show. Running `linear_search()` on it for "Anti-Hero" correctly returns its real index, but `binary_search()` on the same unsorted list incorrectly returns `-1`, even though the song is right there; its smaller/larger comparisons only make sense on sorted data, so they steer it away from the correct answer entirely. This is a concrete demonstration of exactly when binary search cannot be used, and why linear search remains the appropriate choice for this kind of list despite being the theoretically "slower" algorithm.

## Linear Search vs. Binary Search Performance

Linear search makes no assumptions about how a list is organized, which is exactly what makes it usable on any list, sorted or not, at the cost of an O(n) worst case: it may have to check every single element. Binary search trades that flexibility for speed: by requiring the list to be sorted, it can rule out half of the remaining elements with a single comparison, giving it an O(log n) worst case. That trade-off is why binary search wins decisively on the 100,000-entry streaming catalog (17 comparisons vs. up to 100,000), but is completely unusable on the unsorted Recently Played list, where linear search is not just acceptable, but the only algorithm that gives a correct answer.
