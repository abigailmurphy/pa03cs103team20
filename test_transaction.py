import pytest
import sqlite3
import os
from datetime import date
from transaction import Transaction, to_dict, cat_to_dict

@pytest.fixture
def tuples():
    ''' create transaction tuples ~ ariasmithbrandeis'''
    return [(1, 10, 'category1', '02/02/22', 'desc1'),
            (2, 20, 'category2', '03/03/22', 'desc3'),
            (3, 10, 'category1', '01/02/23', 'desc5'),
            (4, 40, 'category2', '03/04/23', 'desc7')]

@pytest.fixture
def returned_tuples(tuples):
    ''' ~ariasmithbrandeis'''
    return [tuples[i] for i in range(len(tuples))]

@pytest.fixture
def returned_dicts(tuples):
    ''' ~ariasmithbrandeis'''
    return [to_dict(t) for t in tuples]

@pytest.fixture
def trans_path(tmp_path):
    ''' ~ariasmithbrandeis'''
    yield tmp_path / 'tracker.db'

@pytest.fixture(autouse=True)
def transactions(trans_path,tuples):
    ''' ~ariasmithbrandeis'''
    "create and initialize the todo.db database in /tmp "
    con= sqlite3.connect(trans_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num INT PRIMARY KEY, amount DOUBLE, 
                    category TEXT, date DATE, description TEXT)''')
    for i in range(len(tuples)):
        cur.execute('''insert into transactions values(?,?,?,?,?)''',tuples[i])
    # create the transactions database
    con.commit()
    td = Transaction(trans_path)
    yield td
    cur.execute('''drop table transactions''')
    con.commit()
  
def test_select_all(transactions, returned_dicts):
    ''' ~ariasmithbrandeis'''
    td = transactions
    results = td.select_all()
    expected = returned_dicts
    assert results == expected

def test_add_transaction(transactions, returned_dicts):
    ''' ~ariasmithbrandeis'''
    td = transactions
    tuple = (len(returned_dicts)+1,50, 'category1', '03/14/23', 'desc9')
    transactions.add_transaction(to_dict(tuple))
    results = td.select_all()
    assert results[-1] == to_dict(tuple)
  
def test_delete_transaction(transactions,returned_dicts):
    ''' ~ariasmithbrandeis'''
    td = transactions
    td.delete_transaction(1)
    results = td.select_all()
    expected = returned_dicts
    assert results == expected[1:]
