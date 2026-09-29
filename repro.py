from split_billing import split_amount_cents

total = 100  # $1.00
splits = split_amount_cents(total, 3)
actual_sum = sum(splits)

print(f"total={total}, splits={splits}, actual_sum={actual_sum}")
if actual_sum != total:
    print(f"BUG DETECTED: Lost {total - actual_sum} cent(s) during split! Sum of parts does not equal total.")
    raise SystemExit(1)
raise SystemExit(0)
