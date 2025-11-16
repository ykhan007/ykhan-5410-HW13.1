# BSSD 3410/5410 - Lesson 13.1 Markov Text Generator (Word-Based)
# Notes:
# - Combines multiple .txt files into one corpus
# - Builds Markov rules on *words* using a sliding window (n-grams)
# - Uses Counter to store frequencies and a simple "temperature" pick
# - Lets you run multiple times without restarting

import math
import random
from collections import Counter, defaultdict

def load_texts(paths):
    """Read multiple text files, lowercase, and split into words."""
    all_words = []
    for p in paths:
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read().lower()
                # very light cleanup; keep punctuation-as-tokens optional
                # here we just split on whitespace to stay close to class flow
                words = text.split()
                all_words.extend(words)
        except FileNotFoundError:
            print(f"Could not find file: {p}")
    return all_words

def make_rules(words, window):
    """
    Build a dict: key = tuple(last 'window' words),
                  value = list of next-words (duplicates kept to reflect frequency).
    Example:
      ('and', 'the') -> ['slithy', 'mome', 'the', ...]
    """
    rules = defaultdict(list)
    if len(words) <= window:
        return rules

    for i in range(len(words) - window):
        key = tuple(words[i:i+window])
        nxt = words[i+window]
        rules[key].append(nxt)
    return rules

def to_counters(rules):
    """
    Convert each list of next-words into Counter sorted by most_common().
    Store as { key: [(word, count), (word, count), ...] } sorted desc by count.
    """
    freq_map = {}
    for key, next_list in rules.items():
        c = Counter(next_list).most_common()
        freq_map[key] = c
    return freq_map

def pick_with_temperature(options_sorted, temp):
    """
    options_sorted: list of (word, count) already sorted by most_common (desc).
    temp in [0,1]:
      0.0 => always pick the top option
      1.0 => pick toward the end of the sorted list
      in-between => mix (we map temp to an index)
    """
    if not options_sorted:
        return None

    # clamp temperature to [0,1]
    t = max(0.0, min(1.0, float(temp)))

    # Index selection using a simple linear map; you can also try non-linear if you want.
    idx = int(round((len(options_sorted) - 1) * t))

    # As a small touch of randomness at temps > 0, consider nudging around idx:
    if t > 0:
        lo = max(0, idx - 1)
        hi = min(len(options_sorted) - 1, idx + 1)
        idx = random.randint(lo, hi)

    return options_sorted[idx][0]

def generate_text(freq_map, window, total_words, temp):
    """
    Generate 'total_words' words.
    Start by picking a random key from the rule set, then extend using frequency map + temperature.
    """
    if not freq_map:
        return "(no output: not enough words or empty rules)"

    # start from a random key (tuple of 'window' words)
    start_key = random.choice(list(freq_map.keys()))
    out_words = list(start_key)

    # If user asks for fewer words than the window, trim
    if total_words <= window:
        return " ".join(out_words[:total_words])

    # Keep predicting the next word from the last 'window' words
    for _ in range(total_words - window):
        key = tuple(out_words[-window:])
        options = freq_map.get(key)
        if not options:
            # backoff: jump to a new random key to avoid stopping prematurely
            key = random.choice(list(freq_map.keys()))
            options = freq_map[key]

        next_word = pick_with_temperature(options, temp)
        if next_word is None:
            break
        out_words.append(next_word)

    return " ".join(out_words)

def main():
    print("=== Markov Text Generator (Words) ===")
    while True:
        try:
            num_files = int(input("How many text files to combine? ").strip())
        except ValueError:
            print("Please enter a number.")
            continue

        paths = []
        for i in range(num_files):
            p = input(f"Path for file #{i+1}: ").strip()
            paths.append(p)

        try:
            window = int(input("Window size (e.g., 2 or 3): ").strip())
            temp = float(input("Temperature (0 to 1): ").strip())
            total_words = int(input("How many words to generate? ").strip())
        except ValueError:
            print("Invalid number. Try again.")
            continue

        words = load_texts(paths)
        if len(words) < window + 1:
            print("Not enough words in your files for that window size. Try smaller window or more text.")
            continue

        rules = make_rules(words, window)
        freq_map = to_counters(rules)

        result = generate_text(freq_map, window, total_words, temp)
        print("\n--- Generated Text ---")
        print(result)
        print("----------------------\n")

        again = input("Generate again with new settings? (y/n): ").strip().lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()

