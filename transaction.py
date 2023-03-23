
import squlite3
import os

  def toDict(t):
    ''' t is a tuple (item_#, amount, category,date,description)'''
    print('t='+str(t))
    tracker = {'item':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return tracker
  
class Transaction():
  
    def __init__(self, dbase):
        self.runQuery('''CREATE TABLE IF NOT EXISTS dbase
                    (item INT PRIMARY KEY, amount DOUBLE, category TEXT, date DATE, description TEXT'''),())
    
    def selectAll(self):
        ''' return all items in tracker as a list of dicts'''
        return self.runQuery("SELECT * FROM tracker",())

    def selectItem(self):
        ''' return all item #'s as a list of dicts.'''
        return self.runQuery("SELECT item from tracker",())
   
    def selectCategories(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.runQuery("SELECT DISTINCT category from tracker",())
      
   def byDate(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.runQuery("SELECT item, date FROM tracker ORDER BY date",())
      
   def byMonth(self):
        ''' return all distinct categories as a list of dicts.'''
        return self.runQuery("SELECT item, date FROM tracker ORDER BY MONTH(date) DESC",())
      
    def addCategory(self, item, cat):
        ''' return updated with category added '''
        return self.runQuery("UPDATE tracker SET category = cat WHERE item=(?)",(item,))

   
    def addTransaction(self,item):
        ''' create a tracker item and add it to the tracker table '''
        return self.runQuery("INSERT INTO tracker VALUES(?,?,?,?,?)",(item['item'],item['amount'],item['date'],item['description']))

    def deleteTransaction(self,item):
        ''' delete a tracker item '''
        return self.runQuery("DELETE FROM tracker WHERE item=(?)",(item,))


    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
    
