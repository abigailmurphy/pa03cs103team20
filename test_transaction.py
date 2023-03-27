import pytest
from transaction import Transaction

def test_to_dict():
  # Test that the to_dict function returns a dictionary with the correct keys and values
    t = (1, 10.0, 'food', '2022-03-26', 'groceries')
    expected_result = {'item_num': 1, 'amount': 10.0, 'category': 'food', 'date': '2022-03-26', 'description': 'groceries'}
    assert Transaction(database).to_dict(t) == expected_result
  
def test_select_all():
  



def test_select_item():
  # Test that the select_item function returns a list of all item numbers as dictionaries
    expected_result = [{'item_num': 1}, {'item_num': 2}, {'item_num': 3}]
    assert Transaction(database).select_item() == expected_result
  

def test_distinct_categories():
  
  
  
  
def test_by_date():
  
  
  
  
  
def test_by_month():
  
  
  
  
def test_by_month_asc_year():
  
  
  
  
  
def test_add_category():
  
  
  
  
def test_add_transaction():
  
  
  
  
  
def test_delete_transaction():
  
  
  
def test_run_query():




