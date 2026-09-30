def split_amount_cents(total_cents: int, num_splits: int) -> list[int]:
    """Split total amount in cents evenly among participants, ensuring sum(splits) == total_cents."""
    if num_splits <= 0:
        raise ValueError("num_splits must be greater than 0")

    # Compute the base share for each participant and the remainder that cannot be evenly divided.
    base_share = total_cents // num_splits
    remainder = total_cents % num_splits

    # Initialise all splits with the base share.
    splits = [base_share] * num_splits

    # Distribute the leftover cents one by one to the first `remainder` splits.
    for i in range(remainder):
        splits[i] += 1

    return splits

    # Initialise all splits with the base share.
    splits = [base_share] * num_splits

    # Distribute the leftover cents one by one to the first `remainder` splits.
    for i in range(remainder):
        splits[i] += 1

    return splits
