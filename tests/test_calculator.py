import taxbill.calculator as calc


def test_single_band_tax_amount():
    assert calc.single_band_tax_amount(10000, 0.2, 12000) == 0
    assert calc.single_band_tax_amount(12000, 0.2, 12000) == 0
    assert calc.single_band_tax_amount(22000, 0.2, 12000) == 2000
