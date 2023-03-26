
import sqlite3
import os

def toDict(t):
    ''' t is a tuple (item_num, amount, category,date,description)'''
    print('t='+str(t))
    tracker = {'item_num':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return tracker
  
class Transaction():
  
    def __init__(self, dbase):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num INT PRIMARY KEY, amount DOUBLE, category TEXT, date DATE, description TEXT''')
        self.dbase = dbase

    def selectAll(self):
        ''' return all items in tracker as a list of dicts'''
        return self.runQuery("SELECT * FROM transactions",())

    def selectItem(self):
        ''' return all item #'s as a list of dicts.'''
        return self.runQuery("SELECT item from transactions",())
   
    def distinctCategories(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.runQuery("SELECT DISTINCT category from transactions",())
      
    def byDate(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.runQuery("SELECT item_num, amount, category, date, description FROM transactions ORDER BY date",())
      
    def byMonth(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.runQuery("SELECT DISTINCT item_num, amount, category, date, description FROM transactions ORDER BY MONTH(date) DESC",())
      
    def byMonthASCYear(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.runQuery("SELECT DISTINCT item_num, amount, category, date, description FROM transactions ORDER BY YEAR(date) DESC",())
      
    def addCategory(self, item_num, cat):
        ''' return updated with category added '''
        return self.runQuery("UPDATE transactons SET category = (?) WHERE item_num=(?)",(cat, item_num,))

   
    def addTransaction(self,item):
        ''' create a transactions item and add it to the transactions table '''
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item_num'],item['amount'],item['date'],item['description']))

    def deleteTransaction(self,item_num):
        ''' delete a transactions item '''
        return self.runQuery("DELETE FROM transactions WHERE item_num=(?)",(item_num,))


    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/'+self.dbase)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
    
