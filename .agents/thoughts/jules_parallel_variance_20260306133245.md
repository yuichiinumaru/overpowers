# Jules Parallel Delegation Variance Report
This report analyzes the pull requests generated in parallel by Jules, comparing their outputs to measure variance in reasoning and code generation for identical tasks.

## Summary Statistics
- **Total Batches Processed:** 43
- **Total PRs Evaluated:** 88
- **Zero-Variance Batches:** 7 (16.3%)
- **Varied Batches:** 36 (83.7%)
- **Average Line Difference (among varied):** 386.4 lines
- **Average Proportional Difference (among varied):** 38.2%

---

## Batch 001
- **Total Parallel PRs:** 3
- **Variance:** DETECTED. The agents produced 3 distinct variations.
- **Line Difference:** 345 lines (Max: 359, Min: 14)
- **Proportional Difference:** 96.1%
  - **Variation 1** (PRs 68): 359 lines.
  - **Variation 2** (PRs 69): 111 lines.
  - **Variation 3** (PRs 127): 14 lines.

## Batch 002
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 241 lines (Max: 350, Min: 109)
- **Proportional Difference:** 68.9%
  - **Variation 1** (PRs 79): 350 lines.
  - **Variation 2** (PRs 80): 109 lines.

## Batch 003
- **Total Parallel PRs:** 1
- **Variance:** NONE (0%). All agents reached the exact same deterministic output.
- **Line Difference:** 0
- **Proportional Difference:** 0.0%

## Batch 008
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 10 lines (Max: 489, Min: 479)
- **Proportional Difference:** 2.0%
  - **Variation 1** (PRs 76): 479 lines.
  - **Variation 2** (PRs 78): 489 lines.

## Batch 009
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 0 lines (Max: 2298, Min: 2298)
- **Proportional Difference:** 0.0%
  - **Variation 1** (PRs 77): 2298 lines.
  - **Variation 2** (PRs 81): 0 lines.

## Batch 012
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 15 lines (Max: 518, Min: 503)
- **Proportional Difference:** 2.9%
  - **Variation 1** (PRs 71): 518 lines.
  - **Variation 2** (PRs 73): 503 lines.

## Batch 013
- **Total Parallel PRs:** 1
- **Variance:** NONE (0%). All agents reached the exact same deterministic output.
- **Line Difference:** 0
- **Proportional Difference:** 0.0%

## Batch 015
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 77 lines (Max: 443, Min: 366)
- **Proportional Difference:** 17.4%
  - **Variation 1** (PRs 90): 443 lines.
  - **Variation 2** (PRs 156): 366 lines.

## Batch 016
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 1155 lines (Max: 1158, Min: 3)
- **Proportional Difference:** 99.7%
  - **Variation 1** (PRs 87): 3 lines.
  - **Variation 2** (PRs 89): 1158 lines.

## Batch 017
- **Total Parallel PRs:** 1
- **Variance:** NONE (0%). All agents reached the exact same deterministic output.
- **Line Difference:** 0
- **Proportional Difference:** 0.0%

## Batch 018
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 76 lines (Max: 762, Min: 686)
- **Proportional Difference:** 10.0%
  - **Variation 1** (PRs 84): 686 lines.
  - **Variation 2** (PRs 88): 762 lines.

## Batch 019
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 368 lines (Max: 391, Min: 23)
- **Proportional Difference:** 94.1%
  - **Variation 1** (PRs 83): 391 lines.
  - **Variation 2** (PRs 85): 23 lines.

## Batch 020
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 336 lines (Max: 757, Min: 421)
- **Proportional Difference:** 44.4%
  - **Variation 1** (PRs 82): 757 lines.
  - **Variation 2** (PRs 147): 421 lines.

## Batch 021
- **Total Parallel PRs:** 1
- **Variance:** NONE (0%). All agents reached the exact same deterministic output.
- **Line Difference:** 0
- **Proportional Difference:** 0.0%

## Batch 022
- **Total Parallel PRs:** 3
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 266 lines (Max: 572, Min: 306)
- **Proportional Difference:** 46.5%
  - **Variation 1** (PRs 103, 148): 306 lines.
  - **Variation 2** (PRs 104): 572 lines.

## Batch 023
- **Total Parallel PRs:** 4
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 200 lines (Max: 505, Min: 305)
- **Proportional Difference:** 39.6%
  - **Variation 1** (PRs 101, 150): 305 lines.
  - **Variation 2** (PRs 102, 149): 505 lines.

## Batch 024
- **Total Parallel PRs:** 4
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 86 lines (Max: 283, Min: 197)
- **Proportional Difference:** 30.4%
  - **Variation 1** (PRs 99, 152): 283 lines.
  - **Variation 2** (PRs 100, 151): 197 lines.

## Batch 025
- **Total Parallel PRs:** 3
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 28 lines (Max: 244, Min: 216)
- **Proportional Difference:** 11.5%
  - **Variation 1** (PRs 97, 154): 244 lines.
  - **Variation 2** (PRs 98): 216 lines.

## Batch 026
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 58 lines (Max: 255, Min: 197)
- **Proportional Difference:** 22.7%
  - **Variation 1** (PRs 95): 255 lines.
  - **Variation 2** (PRs 96): 197 lines.

## Batch 027
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 0 lines (Max: 267, Min: 267)
- **Proportional Difference:** 0.0%
  - **Variation 1** (PRs 93): 267 lines.
  - **Variation 2** (PRs 153): 0 lines.

## Batch 028
- **Total Parallel PRs:** 3
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 1624 lines (Max: 1800, Min: 176)
- **Proportional Difference:** 90.2%
  - **Variation 1** (PRs 92, 146): 1800 lines.
  - **Variation 2** (PRs 94): 176 lines.

## Batch 029
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 308 lines (Max: 920, Min: 612)
- **Proportional Difference:** 33.5%
  - **Variation 1** (PRs 116): 920 lines.
  - **Variation 2** (PRs 117): 612 lines.

## Batch 030
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 887 lines (Max: 1378, Min: 491)
- **Proportional Difference:** 64.4%
  - **Variation 1** (PRs 112): 491 lines.
  - **Variation 2** (PRs 114): 1378 lines.

## Batch 031
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 67 lines (Max: 489, Min: 422)
- **Proportional Difference:** 13.7%
  - **Variation 1** (PRs 109): 422 lines.
  - **Variation 2** (PRs 113): 489 lines.

## Batch 032
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 148 lines (Max: 563, Min: 415)
- **Proportional Difference:** 26.3%
  - **Variation 1** (PRs 108): 415 lines.
  - **Variation 2** (PRs 115): 563 lines.

## Batch 033
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 253 lines (Max: 874, Min: 621)
- **Proportional Difference:** 28.9%
  - **Variation 1** (PRs 107): 621 lines.
  - **Variation 2** (PRs 110): 874 lines.

## Batch 034
- **Total Parallel PRs:** 1
- **Variance:** NONE (0%). All agents reached the exact same deterministic output.
- **Line Difference:** 0
- **Proportional Difference:** 0.0%

## Batch 037
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 211 lines (Max: 885, Min: 674)
- **Proportional Difference:** 23.8%
  - **Variation 1** (PRs 105): 674 lines.
  - **Variation 2** (PRs 106): 885 lines.

## Batch 039
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 0 lines (Max: 1274, Min: 1274)
- **Proportional Difference:** 0.0%
  - **Variation 1** (PRs 125): 0 lines.
  - **Variation 2** (PRs 126): 1274 lines.

## Batch 040
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 0 lines (Max: 17, Min: 17)
- **Proportional Difference:** 0.0%
  - **Variation 1** (PRs 123): 0 lines.
  - **Variation 2** (PRs 124): 17 lines.

## Batch 041
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 2730 lines (Max: 3395, Min: 665)
- **Proportional Difference:** 80.4%
  - **Variation 1** (PRs 129): 665 lines.
  - **Variation 2** (PRs 130): 3395 lines.

## Batch 042
- **Total Parallel PRs:** 1
- **Variance:** NONE (0%). All agents reached the exact same deterministic output.
- **Line Difference:** 0
- **Proportional Difference:** 0.0%

## Batch 043
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 1118 lines (Max: 1752, Min: 634)
- **Proportional Difference:** 63.8%
  - **Variation 1** (PRs 120): 1752 lines.
  - **Variation 2** (PRs 128): 634 lines.

## Batch 044
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 1620 lines (Max: 2054, Min: 434)
- **Proportional Difference:** 78.9%
  - **Variation 1** (PRs 119): 434 lines.
  - **Variation 2** (PRs 155): 2054 lines.

## Batch 045
- **Total Parallel PRs:** 3
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 310 lines (Max: 737, Min: 427)
- **Proportional Difference:** 42.1%
  - **Variation 1** (PRs 118, 142): 427 lines.
  - **Variation 2** (PRs 121): 737 lines.

## Batch 046
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 587 lines (Max: 952, Min: 365)
- **Proportional Difference:** 61.7%
  - **Variation 1** (PRs 141): 952 lines.
  - **Variation 2** (PRs 144): 365 lines.

## Batch 047
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 122 lines (Max: 273, Min: 151)
- **Proportional Difference:** 44.7%
  - **Variation 1** (PRs 143): 273 lines.
  - **Variation 2** (PRs 145): 151 lines.

## Batch 048
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 300 lines (Max: 597, Min: 297)
- **Proportional Difference:** 50.3%
  - **Variation 1** (PRs 139): 297 lines.
  - **Variation 2** (PRs 140): 597 lines.

## Batch 049
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 78 lines (Max: 486, Min: 408)
- **Proportional Difference:** 16.0%
  - **Variation 1** (PRs 136): 408 lines.
  - **Variation 2** (PRs 137): 486 lines.

## Batch 050
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 144 lines (Max: 529, Min: 385)
- **Proportional Difference:** 27.2%
  - **Variation 1** (PRs 132): 385 lines.
  - **Variation 2** (PRs 135): 529 lines.

## Batch 051
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 0 lines (Max: 223, Min: 223)
- **Proportional Difference:** 0.0%
  - **Variation 1** (PRs 133): 0 lines.
  - **Variation 2** (PRs 138): 223 lines.

## Batch 052
- **Total Parallel PRs:** 2
- **Variance:** DETECTED. The agents produced 2 distinct variations.
- **Line Difference:** 141 lines (Max: 326, Min: 185)
- **Proportional Difference:** 43.3%
  - **Variation 1** (PRs 131): 185 lines.
  - **Variation 2** (PRs 134): 326 lines.

## Batch 059
- **Total Parallel PRs:** 1
- **Variance:** NONE (0%). All agents reached the exact same deterministic output.
- **Line Difference:** 0
- **Proportional Difference:** 0.0%

