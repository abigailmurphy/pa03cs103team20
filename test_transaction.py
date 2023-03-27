import pytest
from transaction import Transaction

def database():
    '''monicaiizuka'''
    return Transaction('self.dbase')
  
def test_to_dict():
    '''Test that the to_dict function returns a dictionary with the correct keys and values ~monicaiizuka'''
    t = (1, 10.0, 'Groceries', '2022-03-25', 'Bought groceries')
    expected = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    assert database.to_dict(t) == expected
  
def test_select_all():
    ''' Tests select_all method ~monicaiizuka'''
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
    ''' Tests select_item() method ~monicaiizuka'''
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
    ''' Tests distinct_categories() method ~monicaiizuka'''
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
    ''' Tests by_date() method ~monicaiizuka'''
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
    ''' Tests by_month() method ~monicaiizuka'''
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
    ''' Tests by_month_asc_year() method ~monicaiizuka'''
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
    ''' Tests modify_category() method ~monicaiizuka'''
    t1 = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    t2 = {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'}
    database.add_transaction(t1)
    database.add_transaction(t2)
    database.modify_category('Transportation', 'Travel')
    assert database.select_all() == [t1, {'item_num': 2, 'amount': 20.0, 'category': 'Travel', 'date': '2022-01-02', 'description': 'Filled up gas'}]

  
def test_add_category():
    ''' Tests add_category() method ~monicaiizuka'''
    t1 = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    t2 = {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'}
    database.add_transaction(t1)
    database.add_transaction(t2)
    database.add_category(1, 'Groceries')
    assert database.select_all() == [t1, t2]

def test_add_transaction():
    ''' Tests add_transaction() method ~monicaiizuka'''
    t = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    database.add_transaction(t)
    assert database.select_all() == [t]
  
def test_delete_transaction():
    ''' Tests delete_transaction() method ~monicaiizuka'''
    t1 = {'item_num': 1, 'amount': 10.0, 'category': 'Groceries', 'date': '2022-03-25', 'description': 'Bought groceries'}
    t2 = {'item_num': 2, 'amount': 20.0, 'category': 'Transportation', 'date': '2022-03-26', 'description': 'Filled up gas'}
    database.add_transaction(t1)
    database.add_transaction(t2)
    database.delete_transaction(1)
    assert database.select_all() == [t2]
  
  
