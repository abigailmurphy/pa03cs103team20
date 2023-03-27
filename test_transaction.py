import pytest
from transaction import Transaction

def database():
    return Transaction('self.dbase')
  
def test_to_dict():
  '''Test that the to_dict function returns a dictionary with the correct keys and values'''
    t = (1, 10.0, 'Groceries', '2022-03-25', 'Bought groceries')
    expected_result = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    assert Transaction(database).to_dict(t) == expected_result
  
def test_select_all():
  ''' Tests select_all method '''
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
  ''' Tests select_item() method '''
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
  ''' Tests distinct_categories() method '''
    database.add_transaction({'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'})
    database.add_transaction({'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'})
    database.add_transaction({'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2022-03-27', 'description': 'Watched a movie'})
    database.add_transaction({'item_num': 4, 'amount': 14.0, 'category': 'Transportation', 'date': '2022-03-28', 'description': 'Took a flight'})
    expected =[
        {'category': 'Groceries'}, 
        {'category': 'Transportation'}, 
        {'category': 'Entertainment'}
    ]
    assert database.distinct_categories() == expected
    
 
def test_by_date():
  ''' Tests by_date() method '''
    database.add_transaction({'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'})
    database.add_transaction({'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'})
    database.add_transaction({'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2022-03-27', 'description': 'Watched a movie'})
    expected = [
        {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'},
        {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'},
        {'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2022-03-27', 'description': 'Watched a movie'}
    ]
    assert database.by_date() == expected
  
def test_by_month():
  ''' Tests by_month() method '''
    database.add_transaction({'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'})
    database.add_transaction({'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-01-26', 'description': 'Filled up gas'})
    database.add_transaction({'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2022-09-27', 'description': 'Watched a movie'})
    expected = [
        {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-01-26', 'description': 'Filled up gas'},
        {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'},
        {'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2022-09-27', 'description': 'Watched a movie'}
    ]
    assert database.by_date() == expected
  
  
def test_by_month_asc_year():
  ''' Tests by_month_asc_year() method'''
    database.add_transaction({'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2019-03-25', 'description': 'Bought groceries'})
    database.add_transaction({'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-01-26', 'description': 'Filled up gas'})
    database.add_transaction({'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2003-09-27', 'description': 'Watched a movie'})
    expected = [
        {'item_num': 3, 'amount': 30.0, 'category': 'Entertainment', 'date': '2003-09-27', 'description': 'Watched a movie'},
        {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2019-03-25', 'description': 'Bought groceries'},
        {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-01-26', 'description': 'Filled up gas'}
    ]
    assert database.by_date() == expected
  

def test_modify_category():
  ''' Tests modify_category() method '''
    t1 = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    t2 = {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'}
    database.add_transaction(t1)
    database.add_transaction(t2)
    database.modify_category('Transportation', 'Travel')
    assert database.select_all() == [item1, {'item_num': 2, 'amount': 20.0, 'category': 'Travel', 'date': '2022-01-02', 'description': 'Filled up gas'}]

  
def test_add_category():
  ''' Tests add_category() method '''
    item1 = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    item2 = {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'}
    trans.add_transaction(item1)
    trans.add_transaction(item2)
    trans.add_category(1, 'Groceries')
    assert trans.select_all() == [item1, item2]

def test_add_transaction():
  ''' Tests add_transaction() method '''
    cat = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    database.add_transaction(cat)
    assert database.select_all() == [cat]
  
def test_delete_transaction():
  ''' Tests delete_transaction() method '''
    t1 = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    t2 = {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'}
    database.add_transaction(t1)
    database.add_transaction(t2)
    database.delete_transaction(1)
    assert database.select_all() == [t2]
  
  
