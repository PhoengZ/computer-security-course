# Activity Log

## Trial 1: Review Exercise 1.a and 1.b
- **What was attempted:** Inspected `sol.md`, `count_char.py`, and `image.png` to evaluate accuracy of questions 1.a and 1.b.
- **The hypothesis being tested:** Check whether frequency counts in 1.a (P, R, O) and heuristics in 1.b are correct and complete.
- **The observed result/outcome:**
  - 1.a was incomplete: 'F' also has 6 occurrences (tied with R and O for rank 2-4).
  - 1.b was incomplete: text was truncated mid-sentence, misspelled, and did not list common 2/3-letter words or tie them back to the ciphertext.

## Trial 2: Caesar Cipher Brute-Force Script (Exercise 1.d)
- **What was attempted:** Created `caesar_bruteforce.py` to perform automated brute-force attacks on Caesar ciphertexts assuming no prior knowledge of mappings. Implemented dictionary validation to score candidate plaintexts.
- **The hypothesis being tested:**
  1. A genuine Caesar cipher text with arbitrary shift can be automatically cracked with high confidence (>90%) across 26 shifts in <1 ms.
  2. Running the Caesar brute-force attack on Exercise 1 ciphertext (`PRCSOFQX...`) will yield low confidence (~15%), proving it is a monoalphabetic substitution rather than a uniform Caesar shift.
- **The observed result/outcome:**
  - Demo 1 (Shift 3 Caesar): Automatically identified Shift 3 with 90.9% dictionary match in ~0.9 ms.
  - Demo 2 (Exercise 1 ciphertext): Highest score was only 15.4% (Shift 23), confirming that Exercise 1's ciphertext is a general substitution cipher requiring frequency analysis rather than simple Caesar shifting.

## Trial 3: Simplification of Caesar Brute-Force Code
- **What was attempted:** Refactored `caesar_bruteforce.py` to be minimalist, readable, and simple (~60 lines) using basic Python constructs (`split()`, `strip()`, `sum()`) and clear English console outputs.
- **The hypothesis being tested:** Code can be drastically simplified while retaining full functionality (testing all 26 shifts and dictionary validation).
- **The observed result/outcome:** Clean execution on Windows terminal without encoding issues, accurately testing shifts 0-25 and identifying candidate plaintext.
## Trial 4: Block Cipher Mode Evaluation (ECB vs CBC in Exercise 3)
- **What was attempted:** Integrated image outputs ([images.jpg](file:///C:/Users/USER/Desktop/Comp_sec/ass4/images.jpg), [enc.png](file:///C:/Users/USER/Desktop/Comp_sec/ass4/enc.png), [enc_cbc.png](file:///C:/Users/USER/Desktop/Comp_sec/ass4/enc_cbc.png)) into [sol.md](file:///C:/Users/USER/Desktop/Comp_sec/ass4/sol.md) for Exercise 3, providing commands and visual comparison table.
- **The hypothesis being tested:** ECB mode reveals plaintext structures due to identical blocks encrypting to identical ciphertext, while CBC mode with chaining eliminates repeated patterns, producing pure pseudo-random noise.
## Trial 5: PDF Text Extraction (Sea-Of-Dreams.pdf)
- **What was attempted:** Extracted textual contents from [Sea-Of-Dreams.pdf](file:///C:/Users/USER/Desktop/Comp_sec/ass4/Sea-Of-Dreams.pdf) (332 pages) using `PyMuPDF` (`pymupdf`) and saved to [Sea-Of-Dreams.txt](file:///C:/Users/USER/Desktop/Comp_sec/ass4/Sea-Of-Dreams.txt) with UTF-8 encoding.
- **The hypothesis being tested:** Digital text layer of the PDF is directly extractable without OCR while preserving natural paragraph structure and spacing.
## Trial 6: Exercise 4.a Experimental Design and Table Layout
- **What was attempted:** Formatted and inserted experimental setup outline and performance measurement tables (real time and breakdown) into [sol.md](file:///C:/Users/USER/Desktop/Comp_sec/ass4/sol.md) under Exercise 4.a.
- **The hypothesis being tested:** Structuring the empirical benchmarking process with predefined trials, metrics, and categories standardizes measurement across SHA-1, RC4, Blowfish, and DSA.
## Trial 7: Empirical Benchmark Entry for SHA-1 and RC4
- **What was attempted:** Recorded empirical measurements across 3 trials each for SHA-1 and RC4 in [sol.md](file:///C:/Users/USER/Desktop/Comp_sec/ass4/sol.md), calculating average execution times.
- **The hypothesis being tested:** Evaluating SHA-1 and RC4 on a 1.6MB file yields consistent sub-second execution times with low standard deviation.
## Trial 8: Empirical Benchmark Completion for Blowfish and DSA
- **What was attempted:** Recorded 3 trials each for Blowfish and DSA in [sol.md](file:///C:/Users/USER/Desktop/Comp_sec/ass4/sol.md) and finalized the comparison tables.
- **The hypothesis being tested:** DSA signing duration is predominantly bounded by SHA-1 hashing overhead (~0.071s vs 0.073s), while Blowfish (~0.204s) exhibits performance comparable to RC4 (~0.222s).
- **The observed result/outcome:** Completed performance measurement tables for all 4 primitives in [sol.md](file:///C:/Users/USER/Desktop/Comp_sec/ass4/sol.md).

## Trial 9: Comprehensive Audit and Verification of sol.md
- **What was attempted:** Conducted a comprehensive technical and theoretical audit of all answers in `sol.md` (Exercises 1 through 4) against the assignment requirements in `274_Ch06-Activity IV-Basic Encryption.pdf`.
- **The hypothesis being tested:** Identifying inaccuracies, theoretical misconceptions, and missing academic criteria (such as non-repudiation, Kasiski complexity reduction, RC4 keystream state mechanics, and message integrity vs encryption in digital signatures).
- **The observed result/outcome:** Identified specific conceptual errors in Exercises 1.b, 1.d, 2.a, 4.b, and 4.c, along with typos. Formulated an Implementation Plan for user review and approval before editing.
