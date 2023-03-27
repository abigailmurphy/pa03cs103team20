import pytest
from transaction import Transaction

def database():
    return Transaction('example')
  
def test_to_dict():
  # Test that the to_dict function returns a dictionary with the correct keys and values
    t = (1, 10.0, 'food', '2022-03-26', 'groceries')
    expected_result = {'item_num': 1, 'amount': 10.0, 'category': 'food', 'date': '2022-03-26', 'description': 'groceries'}
    assert Transaction(database).to_dict(t) == expected_result
  
def test_select_all():
  # Add some test transactions to the database
    database.add_transaction({'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'})
    database.add_transaction({'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'})
    database.add_transaction({'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2022-03-27', 'description': 'Watched a movie'})
    expected = [
        {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'},
        {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'},
        {'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2022-03-27', 'description': 'Watched a movie'}
    ]
    assert database.select_all() == expected

def test_select_item():
  # Add some test transactions to the database
    database.add_transaction({'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'})
    database.add_transaction({'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'})
    database.add_transaction({'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2022-03-27', 'description': 'Watched a movie'})
    expected = [
        {'item': 1},
        {'item': 2},
        {'item': 3}
    ]
    assert database.select_item() == expected
  

def test_distinct_categories():
  
  
  
  
def test_by_date():
  
  
  
  
  
def test_by_month():
  
  
  
  
def test_by_month_asc_year():
  
  
  
  
  
def test_add_category():
  
  
  
  
def test_add_transaction():
  
  
  
  
  
def test_delete_transaction():
  
  
  
def test_run_query():




