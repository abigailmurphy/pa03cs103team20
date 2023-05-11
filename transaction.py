import sqlite3
import os

def to_dict(t):
    ''' t is a tuple (item_num, amount, category,date,description) ~abigailmurphy'''
    print('t='+str(t))
    tracker = {'item_num':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return tracker

def cat_to_dict(t):
    '''t is a tuple representing Catagories ~ariasmith'''
    print('t='+str(t))
    tracker = {'category':t[0]}
    return tracker

def sum_to_dict(t):
    '''t is a tuple representing Summaries ~ariasmith'''
    print('t='+str(t))
    tracker = {'count':t[0],'summary':t[1]}
    return tracker

class Transaction:
    '''CRUD SQL for the transactions table'''
    def __init__(self, database):
        '''~abigailmurphy ~ariasmith'''
        self.dbase = database
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num INT PRIMARY KEY, amount DOUBLE, category TEXT,
                      date TIMESTAMP, description TEXT)''',() )
    def select_all(self):
        ''' return all items in tracker as a list of dicts ~abigailmurphy ~ariasmith'''
        return self.run_query("SELECT * FROM transactions ORDER BY item_num",())

    def select_item(self):
        ''' return all item #'s as a list of dicts. ~abigailmurphy ~ariasmith'''
        return self.run_query("SELECT item from transactions",())
    def distinct_categories(self):
        ''' return all distinct categories as a list of dicts. ~abigailmurphy ~ariasmith'''
        return self.run_cat_query("SELECT DISTINCT category from transactions",())
    def by_date(self):
        ''' return counts of transactions by date. ~ariasmith'''
        return self.run_summary_query('''SELECT COUNT(item_num), date
                            FROM transactions group by date ORDER BY date''',())
    def by_month(self):
        ''' return all distinct categories as a list of dicts. ~ariasmith'''
        return self.run_summary_query('''SELECT COUNT(item_num), STRFTIME('%m',date) AS the_date
                              FROM transactions 
                              GROUP BY STRFTIME('%m',date)''',())
    def by_year(self):
        ''' return all distinct categories as a list of dicts. ~ariasmith'''
        return self.run_summary_query('''SELECT COUNT(item_num), STRFTIME('%Y',date) as date
                              FROM transactions 
                              GROUP BY STRFTIME('%Y',date) 
                              ORDER BY date''',())
    def by_category(self):
        ''' return all distinct categories as a list of dicts. ~ariasmith'''
        return self.run_summary_query('''SELECT COUNT(item_num), category
                              FROM transactions 
                              GROUP BY category 
                              ORDER BY category''',())
    def modify_category(self, old_cat, cat):
        ''' return updated with category added ~ariasmith'''
        return self.run_query('''UPDATE transactions SET category=(?)
                                 WHERE category=(?)''',(cat, old_cat,))
    def add_category(self, item_num, cat):
        ''' return updated with category added ~ariasmith'''
        return self.run_query('''UPDATE transactions SET category=(?)
                                WHERE item_num=(?)''',(cat, item_num,))
    def add_transaction(self,item):
        ''' create a transaction and add it to the transactions table ~abigailmurphy ~ariasmith'''
        return self.run_query('''INSERT INTO transactions VALUES(?,?,?,?,?)''',
                              (item['item_num'],
                               item['amount'],
                               item['category'],
                               item['date'],
                               item['description']))

    def delete_transaction(self,item_num):
        ''' delete a transactions item '~abigailmurphy'''
        return self.run_query("DELETE FROM transactions WHERE item_num=(?)",(item_num,))

    def run_query(self,query,tuple):
        ''' return all of the transaction as a list of dicts. ~abigailmurphy, ariasmithbrandeis'''
        con= sqlite3.connect(os.getenv('HOME')+'/'+ self.dbase)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
    def run_cat_query(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts. ~ariasmithbrandeis'''
        con= sqlite3.connect(os.getenv('HOME')+'/'+ self.dbase)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [cat_to_dict(t) for t in tuples]
    def run_summary_query(self,query,tuple):
        ''' return all of the summaries as a list of dicts. ~ariasmithbrandeis'''
        con= sqlite3.connect(os.getenv('HOME')+'/'+ self.dbase)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [sum_to_dict(t) for t in tuples]
