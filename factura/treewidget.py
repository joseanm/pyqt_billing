'''
Created on 14/08/2011

@author: Luis Carlos Mejia
'''
from PyQt4.QtGui import QTreeView, QMessageBox
from PyQt4.QtCore import Qt,SIGNAL,QModelIndex,QAbstractItemModel, QVariant,QString, pyqtSlot
from bisect import insort, bisect_left
from PyQt4.QtSql import QSqlQuery, QSqlDatabase
from herramientas.moneyfmt import moneyfmt
from decimal import Decimal

NODE = 1
KEY = 0

class TreeOfTableWidget(QTreeView):
    def __init__(self,parent = None):
        '''
        Constructor
        '''
        super(TreeOfTableWidget,self).__init__(parent)
#        self.setSelectionBehavior(QTreeView.SelectItems)
        self.setUniformRowHeights(True)
        model = TreeOfTableModel()
        self.setModel(model)
        self.connect(self, SIGNAL("expanded(QModelIndex"),self.expanded)
        self.headers = []
        
#        self.emit(SIGNAL("doubleClicked"),self.model().asRecord(index))
    def currentFields(self):
        return self.model().asRecord(self.currentIndex())
    def expanded(self):
        for column in range(self.model().columnCount(QModelIndex)):
            self.resizeColumnToContents(column)
    
    def update(self,query):
        model = TreeOfTableModel()
        model.headers = self.headers
        model.load(query)
        self.setModel(model)
        

class BranchNode (object):
    def __init__(self,name, parent = None):
        super(BranchNode,self).__init__()
        self.name = name
        self.parent = parent
        self.children = []
        
    def orderKey(self):
        return self.name.lower()
    
    def toString(self):
        return self.name
    
    def __len__(self):
        return len(self.children)
    
    def childAtRow(self,row):
        assert 0 <= row < len(self.children)
        return self.children[row][NODE]
    
    def rowOfChild(self,child):
        for i, item in enumerate(self.children):
            if item[NODE] == child:
                return i
        return -1
    
    def childWithKey(self,key):
        if not self.children:
            return None
        
        i = bisect_left(self.children,(key,None))
        if i <0 or i >= len(self.children):
            return None
        
        if self.children[i][KEY] == key:
            return self.children[i][NODE]
        return None
    
    def insertChild(self,child):
        child.parent = self
        insort(self.children, (child.orderKey(),child))
    
    def hasLeaves(self):
        if not self.children:
            return False
        return isinstance(self.children[0], LeafNode)  

class LeafNode(object):
    def __init__(self,fields,parent = None):
        super(LeafNode,self).__init__()
        self.parent = parent
        self.fields = fields
        
    def orderKey(self):
        return u"\t".join(self.fields).lower()
    
    def toString(self,separator = "\t"):
        return separator.join(self.fields)
    
    def __len__(self):
        return len(self.fields)
    
    def field(self,column):
        assert 0 <= column < len(self.fields)
        
        return self.fields[column]
    
    def asRecord(self):
        record = []
        branch = self.parent
        while branch is not None:
            record.insert(0, branch.toString())
            branch = branch.parent
        assert record and not record[0]
        # Crea un arreglo partiendo de la posicion provista antes de los dos puntos :
        record = record[1:]
        return record + self.fields
     
class TreeOfTableModel( QAbstractItemModel ):
    def __init__( self, parent = None ):
        super( TreeOfTableModel, self ).__init__( parent )
        self.columns = 0
        self.root = BranchNode("")
        self.headers = []
        
        
    def load(self,query):
        self.nesting = 1
        self.root = BranchNode("")
        try:
            query = QSqlQuery( query )
            if not query.exec_():
                raise Exception( "No se pudieron recuperar las categorias" )
            
            self.columns = query.record().count() 
            print query.size()
            if query.size()>0:
                while query.next():
                    fields= []
                    for i in range (self.columns):
                        fields.append(str(query.value(i)))             
                    self.addRecord(fields, False) 

    
        except Exception as inst:
            print  unicode( inst ) 
            return False

    def addRecord(self,fields,callReset=True):
        root = self.root
        branch = None
        for i in range(self.nesting):
            key = fields[i].lower()
            
            branch = root.childWithKey(key)
            if branch is not None:
                root = branch
            else:
                branch = BranchNode(fields[i])
                root.insertChild(branch)
                root = branch
        assert branch is not None
        
        items = fields[self.nesting:]
        
        self.columns = max(self.columns,len(items))
        branch.insertChild(LeafNode(items,branch))
        if callReset:
            self.reset()
    
    def asRecord(self,index):
        
        leaf = self.nodeFromIndex(index)
        
        if leaf is not None and isinstance(leaf, LeafNode):
            
            return leaf.asRecord()
        return []
    
    def rowCount(self,parent):
        node = self.nodeFromIndex(parent)
        if node is None or isinstance(node,LeafNode):
            return 0
        return len(node)
    
    def columnCount(self,parent):
        return self.columns -1
    
    def data(self, index, role):
        if role == Qt.TextAlignmentRole:
            return int(Qt.AlignTop | Qt.AlignLeft)
        
        if role != Qt.DisplayRole:
            return None
        node = self.nodeFromIndex(index)
        assert node is not None
        if isinstance(node,BranchNode):
            return node.toString() if index.column() == 0 else QString("")
        column = index.column()
        if column == 1:
            return moneyfmt(Decimal((node.field(index.column()))),2,"C$ ")
        else:
            return node.field(index.column())
        
    def headerData(self,section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
#            assert 0 <= section <= len(self.headers)  
            return self.headers[section]
            
        return None 
    
    def index(self,row, column, parent):
        assert self.root
        branch = self.nodeFromIndex(parent)
        assert branch is not None
        return self.createIndex(row,column, branch.childAtRow(row))
    
    def parent(self,child):
        node = self.nodeFromIndex(child)
        if node is None:
            return QModelIndex()
        try:
            parent = node.parent
        except:
            parent = None
        if parent is None:
            return QModelIndex()
        grandparent = parent.parent
        if grandparent is None:
            return QModelIndex()
        row = grandparent.rowOfChild(parent)
        assert row != -1
        return self.createIndex(row, 0 , parent ) 
    
    def nodeFromIndex(self,index):
        
        return index.internalPointer() if index.isValid() else self.root
    