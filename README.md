# Currency Rounding Bug

High-level bug: `split_amount_cents` uses simple integer floor division `total_cents // num_splits` without distributing the remainder. In uneven splits (such as dividing $1.00 among 3 parties), the sum of splits equals 99 cents, causing a 1 cent financial reconciliation discrepancy.

Run the reproduction with:

```powershell
python repro.py
```

Run the failing test with:

```powershell
python -m pytest -q
```

Expected result: `split_amount_cents(100, 3)` should distribute the 1 remainder cent so `sum(splits) == 100` (e.g. `[34, 33, 33]`), but the buggy implementation returns `[33, 33, 33]` which totals `99`.
