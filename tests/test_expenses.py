import sys
import os

sys.path.append(os.path.abspath("src"))

from main import transactions

def test_transactions_empty():
    transactions.clear()
    assert transactions == []


def test_add_transaction():
    transactions.clear()

    transactions.append(
        {
            "amount": 500,
            "category": "еда",
        }
    )

    assert len(transactions) == 1


def test_transaction_amount():
    transactions.clear()

    transactions.append(
        {
            "amount": 1500,
            "category": "транспорт",
        }
    )

    assert transactions[0]["amount"] == 1500