# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two fundamental linear data structures in Python: the Stack (LIFO — Last In, First Out) and the Queue (FIFO — First In, First Out). I implemented both from scratch and demonstrated their behavior using real-world scenarios.

## What I Built

### `Stack` (TODO 1)

Backed by a plain Python list. `push()` appends to the end of the list, and `pop()` removes from that same end — the two operations sharing one end is what makes it LIFO. `peek()` returns the top value without removing it, and `is_empty()` checks the list's length. Both `pop()` and `peek()` raise `IndexError` on an empty stack, matching the same exception type Python's own `list.pop()` raises on an empty list.

### `Queue` (TODO 2)

Backed by `collections.deque` instead of a list. `enqueue()` appends to the back; `dequeue()` removes from the front with `popleft()`. I used `deque` specifically because `deque.popleft()` is O(1), while removing from the front of a plain list (`list.pop(0)`) is O(n) — every remaining element has to shift left by one. `front()` returns the next value without removing it, and both `dequeue()` and `front()` raise `IndexError` on an empty queue, for the same reason as the stack.

### Stack Demonstration — `demonstrate_stack()` (TODO 3)

Uses a browser back-button history as the real-world scenario: four pages are pushed onto the stack, then popped one at a time to show that the most recently visited page ("checkout.html") is the first one `pop()` returns — LIFO order.

### Queue Demonstration — `demonstrate_queue()` (TODO 4)

Uses a customer support ticket queue as the real-world scenario: four tickets are enqueued, then dequeued one at a time to show that the first ticket submitted ("Ticket #101") is the first one served — FIFO order.

### Edge Cases (TODO 5)

Both demo functions test:
- Popping/dequeuing from an empty collection (raises `IndexError`, caught and reported).
- Peeking/checking the front of an empty collection (same).
- A single-item stack/queue that becomes empty again after one removal.

### Real-World Scenario (TODO 6)

The browser-history stack and support-ticket queue **are** the real-world scenarios — chosen because they're the clearest everyday examples of LIFO and FIFO behavior, respectively, rather than adding a separate abstract example on top of the demo functions.

## Memory Usage

Both structures grow linearly with the number of items stored — O(n) space. The `Stack`'s underlying Python list over-allocates extra capacity as it grows, so most `push()` calls don't need to resize; occasionally the list resizes to a larger block and copies existing elements over, but this happens rarely enough that appends stay O(1) on average. The `Queue`'s `deque` is implemented as a series of fixed-size blocks rather than one contiguous array, so it grows by linking in new blocks as needed instead of copying existing data — memory usage still scales linearly with the number of items, without ever needing a full-array copy.

## Stacks vs. Queues in Real-World Applications

A stack fits situations where the most recent action needs to be undone or revisited first — browser back buttons, undo/redo history in an editor, or function call stacks. A queue fits situations where fairness and order of arrival matter — support tickets, print jobs, or task scheduling, where the first request in should be the first one handled.

## How to Run

```bash
python3 unit2_discussion.py
```
