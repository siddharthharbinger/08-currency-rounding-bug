def split_amount_cents(total_cents: int, num_splits: int) -> list[int]:
    """Split total amount in cents evenly among participants, ensuring sum(splits) == total_cents."""
    if num_splits <= 0:
        raise ValueError("num_splits must be greater than 0")

    # Bug: floor division without distributing remainder causes lost cents
    base_share = total_cents // num_splits
    return [base_share] * num_splits
