import taxbill.calculator as calc


def test_single_band_tax_amount():
    assert calc.single_band_tax_amount(10000, 0.2, 12000) == 0
    assert calc.single_band_tax_amount(12000, 0.2, 12000) == 0
    assert calc.single_band_tax_amount(22000, 0.2, 12000) == 2000


def test_tax_amount():
    bands = [
        {"threshold": 0, "limit": 10000, "rate": 0},
        {"threshold": 10000, "limit": 40000, "rate": 0.2},
        {"threshold": 40000, "limit": 100000, "rate": 0.4},
    ]
    assert calc.tax_amount(5000, bands) == 0
    assert calc.tax_amount(10000, bands) == 0
    assert calc.tax_amount(15000, bands) == 1000
    assert calc.tax_amount(40000, bands) == 6000
    assert calc.tax_amount(100000, bands) == 30000
    