
import squlite3
import os

  def toDict(t):
    ''' t is a tuple (item, amount, category,date,description)'''
    print('t='+str(t))
    tracker = {'item':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return tracker
  
class Transaction():
  
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS tracker
                    (item INT PRIMARY KEY, amount DOUBLE, category TEXT, date TEXT, description TEXT'''),())
    
    def selectAll(self):
        ''' return all items in tracker as a list of dicts'''
        return self.runQuery("SELECT * FROM tracker",())

    def selectItem(self):
        ''' return all item #'s as a list of dicts.'''
        return self.runQuery("SELECT item,* from tracker",())

   
    def add(self,item):
        ''' create a tracker item and add it to the tracker table '''
        return self.runQuery("INSERT INTO tracker VALUES(?,?,?,?,?)",(item['item'],item['amount'],item['category'],item['date'],item['description']))

    def delete(self,item):
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
    
    
