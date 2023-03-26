
import sqlite3
import os

def to_dict(t):
    ''' t is a tuple (item_num, amount, category,date,description)'''
    print('t='+str(t))
    tracker = {'item_num':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return tracker
  
class Transaction:

    def __init__(self, database):
        self.dbase = database
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num INT PRIMARY KEY, amount DOUBLE, category TEXT, date DATE, description TEXT)''',() )
        

    def select_all(self):
        ''' return all items in tracker as a list of dicts'''
        return self.run_query("SELECT * FROM transactions",())

    def select_item(self):
        ''' return all item #'s as a list of dicts.'''
        return self.run_query("SELECT item from transactions",())
   
    def distinct_categories(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.run_query("SELECT DISTINCT category from transactions",())
      
    def by_date(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.run_query("SELECT item_num, amount, category, date, description FROM transactions ORDER BY date",())
      
    def by_month(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.run_query("SELECT DISTINCT item_num, amount, category, date, description FROM transactions ORDER BY MONTH(date) DESC",())
      
    def by_month_asc_year(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.run_query("SELECT DISTINCT item_num, amount, category, date, description FROM transactions ORDER BY YEAR(date) DESC",())
      
    def add_category(self, item_num, cat):
        ''' return updated with category added '''
        return self.run_query("UPDATE transactons SET category = (?) WHERE item_num=(?)",(cat, item_num,))

   
    def add_transaction(self,item):
        ''' create a transactions item and add it to the transactions table '''
        return self.run_query("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item_num'],item['amount'],item['category'],item['date'],item['description']))

    def delete_transaction(self,item_num):
        ''' delete a transactions item '''
        return self.run_query("DELETE FROM transactions WHERE item_num=(?)",(item_num,))


    def run_query(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/'+ self.dbase)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
    
    
