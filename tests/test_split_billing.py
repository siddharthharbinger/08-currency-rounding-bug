from split_billing import split_amount_cents


def test_split_amount_conserves_total():
    splits = split_amount_cents(100, 3)
    assert sum(splits) == 100
    assert splits in ([34, 33, 33], [33, 34, 33], [33, 33, 34])


def test_split_amount_exact_division():
    splits = split_amount_cents(90, 3)
    assert splits == [30, 30, 30]
    assert sum(splits) == 90
