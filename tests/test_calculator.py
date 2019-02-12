import taxbill.calculator as calc

RATES = {
    "employees_ni": [
        {"threshold": 6000, "limit": 8000, "rate": 0},
        {"threshold": 8000, "limit": 40000, "rate": 0.1},
        {"threshold": 40000, "limit": 10000, "rate": 0.02},
    ],
    "employers_ni": [
        {"threshold": 6000, "limit": 8000, "rate": 0},
        {"threshold": 8000, "limit": 40000, "rate": 0.15},
    ],
    "income_tax_earnings": [
        {"threshold": 0, "limit": 10000, "rate": 0},
        {"threshold": 10000, "limit": 40000, "rate": 0.2},
        {"threshold": 40000, "limit": 100000, "rate": 0.4},
    ],
}


def test_single_band_tax_amount():
    assert calc.single_band_tax_amount(10000, 0.2, 12000) == 0
    assert calc.single_band_tax_amount(12000, 0.2, 12000) == 0
    assert calc.single_band_tax_amount(22000, 0.2, 12000) == 2000


def test_tax_amount():
    assert calc.tax_amount(5000, RATES["income_tax_earnings"]) == 0
    assert calc.tax_amount(10000, RATES["income_tax_earnings"]) == 0
    assert calc.tax_amount(15000, RATES["income_tax_earnings"]) == 1000
    assert calc.tax_amount(40000, RATES["income_tax_earnings"]) == 6000
    assert calc.tax_amount(100000, RATES["income_tax_earnings"]) == 30000


def test_salary_taxes():
    assert calc.salary_taxes(8000, RATES) == {
        "employees_ni": 0,
        "employers_ni": 0,
        "income_tax_earnings": 0,
    }

    assert calc.salary_taxes(10000, RATES) == {
        "employees_ni": 200,
        "employers_ni": 300,
        "income_tax_earnings": 0,
    }

    assert calc.salary_taxes(20000, RATES) == {
        "employees_ni": 1200,
        "employers_ni": 1800,
        "income_tax_earnings": 2000,
    }
