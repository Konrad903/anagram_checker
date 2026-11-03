
---

## `Anagram.py` (CLI Anagram Checker)

```markdown
# 🔤 Anagram Checker — Command-Line Utility

A small **object-oriented** Python script that checks whether two words are anagrams. Uses the sorted-character comparison technique — the cleanest and most reliable way to detect anagrams.

---

## 📌 Project Overview

An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once (e.g., *listen* and *silent*). This project implements anagram detection via a `class` with `__init__` and a `display` method.

## ⚙️ How It Works

1. On instantiation, the `anagram` class prompts the user for two strings.
2. The `display` method calls `sorted(str1) == sorted(str2)`.
3. If the sorted lists match, the strings share the same character multiset and therefore are anagrams.
4. The result is printed.

## ✨ Features

- **Class-based design** — a clean pattern for stateful logic.
- **O(1) comparison after sorting** — no manual counting loops needed.
- **Handles duplicates correctly** — `"aabbc"` vs `"cabba"` correctly identified.

## ▶️ How to Run

```bash
python Anagram.py
