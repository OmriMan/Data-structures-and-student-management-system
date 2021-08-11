import copy
from functools import total_ordering
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    
    def __repr__(self):
        return '[' + str(self.value) + ']'


class Tree_node():
    def __init__(self, key, val):
        self.key    = key
        self.val     = val
        self.left    = None
        self.right = None

    def __repr__(self):
         return str(self.key) + ": " + str(self.val)
        
    def is_leaf(self):
        return (self.left == None) and (self.right == None)
    
    def find_successor(self):
        if self.right is None:
            return None
        tmp = self.right
        while tmp.left is not None:
            tmp = tmp.left
        return tmp
        
    
class Binary_search_tree():
    def __init__(self):
        self.root = None

    def search(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)
    
    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val     # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else: #key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return
        
        if self.root == None: #empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)
            
    def find_parent(self,key):
        parent = self.root
        children = self.root
        
        if self.root.key == key:
            return None,self.root
        
        while children.key != key:
            parent = children
            if parent.key > key:
                if parent.left is not None:
                    children = parent.left
                else:
                    return
            elif parent.key < key:
                if parent.right is not None:
                    children = parent.right
                else:
                    return
            else:
                break
        return parent, children

    def delete(self, key):
        if not self.search(key):
            return
        parent, children = self.find_parent(key)
        if children.is_leaf(): # basic case
            if parent is not None:
                if children.key > parent.key:
                    parent.right = None
                else:
                    parent.left = None
                    
            else:
                self.root = None

        elif children.left is None: # has one children - right
            if parent is not None:
                if children.key > parent.key: 
                    parent.right = children.right
                else:
                    parent.left = children.right
            else:
                self.root = children.right
                
        elif children.right is None: # has one children - left
            if parent is not None:
                if children.key < parent.key:
                    parent.left = children.left
                else:
                    parent.right = children.left
            else:
                self.root = children.left
                
        else: # complicate case - 2 children
            successor = children.find_successor()
            successor_parent, successor = self.find_parent(successor.key)
            if successor.right is not None:
                if successor_parent.key != key: # successor_parent shouldn't be deleted
                    successor_parent.left = successor.right
                else:
                    if children.key > parent.key: 
                        parent.right = children.right
                    else:
                        parent.left = children.right
            else: #successor is leaf
                    if successor_parent.key > successor.key:
                        successor_parent.left = None
                    else:
                        successor_parent.right = None
                    children.key = successor.key
                    children.val = successor.val
                        
    def inorder(self):
        ''' return inorder traversal of values as str, uses recursion '''
        def inorder_rec(curr_node , res):
            if curr_node != None:
                inorder_rec(curr_node.left , res)
                res.append((curr_node.key , curr_node.val ))
                inorder_rec(curr_node.right , res)
            return res
            
        if self.root == None: #empty tree
            return []
        else:
            return inorder_rec(self.root, [])
        
            
    def __repr__(self): 
        #no need to understand the implementation of this one
        out = ""
        #need printree.py file or make sure to run it in the NB
        for row in printree(self.root): 
            out = out + row + "\n"
        return out
                
    



def printree(t, bykey = True):
        """Print a textual representation of t
        bykey=True: show keys instead of values"""
        #for row in trepr(t, bykey):
        #        print(row)
        return trepr(t, bykey)

def trepr(t, bykey = False):
        """Return a list of textual representations of the levels in t
        bykey=True: show keys instead of values"""
        if t==None:
                return ["#"]

        thistr = str(t.key) if bykey else str(t.val)
        return conc(trepr(t.left,bykey), thistr, trepr(t.right,bykey))

def conc(left,root,right):
        """Return a concatenation of textual represantations of
        a root node, its left node, and its right node
        root is a string, and left and right are lists of strings"""
        
        lwid = len(left[-1])
        rwid = len(right[-1])
        rootwid = len(root)
        
        result = [(lwid+1)*" " + root + (rwid+1)*" "]
        
        ls = leftspace(left[0])
        rs = rightspace(right[0])
        result.append(ls*" " + (lwid-ls)*"_" + "/" + rootwid*" " + "\\" + rs*"_" + (rwid-rs)*" ")
        
        for i in range(max(len(left),len(right))):
                row = ""
                if i<len(left):
                        row += left[i]
                else:
                        row += lwid*" "

                row += (rootwid+2)*" "
                
                if i<len(right):
                        row += right[i]
                else:
                        row += rwid*" "
                        
                result.append(row)
                
        return result

def leftspace(row):
        """helper for conc"""
        #row is the first row of a left node
        #returns the index of where the second whitespace starts
        i = len(row)-1
        while row[i]==" ":
                i-=1
        return i+1

def rightspace(row):
        """helper for conc"""
        #row is the first row of a right node
        #returns the index of where the first whitespace ends
        i = 0
        while row[i]==" ":
                i+=1
        return i
   
class Subject:
    '''
    This class represents courses for students
    '''
    def __init__(self,name,grade,points):
        '''
        Constructor.
        '''
        self.name = name
        self.grade = float(grade)
        self.points = float(points)
    def __eq__(self,other):
        return self.grade==other.grade and self.name==other.name and self.points==other.points
    def __repr__(self):
        '''
        repr overload
        '''
        return (self.name +', '+str(self.grade)+str([self.points]))

@total_ordering   
class Student:
    '''
    This class represents student
    '''
    def __init__(self, name, student_id):
        '''
        Constructor
        '''
        self.name = name
        self.student_id = student_id
        self.head = None
        self.points = float(0.0)
    
    def add_subjects(self,lst):
        '''
        function that add subjects to this student(self)
        param lst - list of the subjects
        return None
        '''
        if self.head == None:#no subject for this student
            p = Node(lst[0])
            self.head = p
            if lst[0].grade>=56:
                self.points+=lst[0].points
            del lst[0]
        copypy = copy.deepcopy(lst)
        for i in copypy:#run on copy for not miss elements
            x=self.head
            while x!=None:#if subject already in the student linked list-update this subject 
                if i.name == x.value.name:
                    #if this student fail in course - dont count the points of this course
                    if i.grade>=56 and x.value.grade<56:
                        self.points+=i.points
                    elif i.grade<56 and x.value.grade>=56:
                        self.points+=-(i.points)
                    #z=Node(i)
                    x.value = i
                    lst.remove(i)
                    break
                x=x.next
        for i in lst:#add the subjects that never been in this student's list
            y=self.head
            while y!=None:
                if i.grade>=56:
                    self.points+=i.points
                p = self.head
                pok = Node(i)
                pok.next = p
                self.head = pok
                if y.next == None:    
                    y=y.next
                else:
                    break
                
    def get_subjects(self):
        if self.head == None:return None
        sub_list=[]
        x=self.head
        while x!=None:
            sub_list.append(x.value)
            x=x.next
        return sub_list
    
    def get_subjects_names(self):
        if self.head == None:return None
        sub_list=[]
        x=self.head
        while x!=None:
            sub_list.append(x.value.name)
            x=x.next
        return sub_list
        
    
    def get_average(self):
        '''
        function that return the student avg grades
        return float
        '''
        x=self.head
        sum_grades = 0
        total_points = 0
        if self.head == None:
            return 0.0
        while x.next!=None:
            sg = x.value.grade#subject grade
            sp = x.value.points#subject points
            sum_grades+= sg*sp#update the sum of the grades according to the grade and the point of a subject
            total_points+=sp#update the student points
            x = x.next
        if x.next == None:#last element in the student subjects list
            sg = x.value.grade
            sp = x.value.points
            sum_grades+= sg*sp
            total_points+=sp
        return sum_grades/total_points
    
    def __gt__(self,other):
        return self.get_average()>other.get_average()
    def __eq__(self,other):
        return self.get_average()==other.get_average()
    
    def is_warning(self):
        '''
        return True if the student in warning,else return False
        '''
        if self.head==None:
            return False
        if self.get_average()<=65:
            return True
        fail_counter = 0#count the fails
        x=self.head
        while x!=None:
            if not x.value.grade>=56:
                fail_counter+=1
            x=x.next
        if fail_counter>=2:
            return True
        return False
     
    def __repr__(self):
        '''
        repr overload
        '''
        stu_id =[self.student_id]
        if self.head==None:
            subs = 'no subjects yet'
        else:
            x=self.head
            subs = str(x.value.name)+'('+str((x.value.points))+')'+'-'+str(x.value.grade)
            x=x.next
            while x!=None:
                subs = subs+', '+str(x.value.name)+'('+str((x.value.points))+')'+'-'+str(x.value.grade)
                x=x.next
        subs = subs+'.'
        y=self.head
        real_points=float(0.0)
        while y!=None:
            if y.value.grade>=56:
                real_points+=y.value.points
            y=y.next
        self.points = real_points
        return ('Student '+self.name+str(stu_id) +', ' +'avg:'+str(self.get_average())+', '+'points:'+str(self.points)+', '+'grades:'+subs)
    

                
class ForeignStudent(Student):
    '''
    This class represents foreign student(inheritance class of student class)
    '''
    def __init__(self,name, student_id):
        Student.__init__(self,  name, student_id)
    def get_average(self):
        '''
        function that return Foreign student avg grades
        return float
        '''
        x=self.head
        gr_lst = []#student's gardes list
        while x!=None:
            gr_lst.append(x.value.grade)
            x=x.next
        if gr_lst==[]:
            return 0.0
        return (Student.get_average(self)+max(gr_lst))/2#regular student avg+max garde /2
    def __repr__(self):
        '''
        repr overload
        '''
        return 'Foreign'+Student.__repr__(self)
               
class Queue:
    '''
    This class represents queue,last element in self.queue[0] and first in self.queue[-1]
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.queue = []
    def enqueue(self,val):
        '''
        function that enter the val to the end of the queue
        '''
        self.queue.insert(0,val)
    def dequeue(self):
        '''
        function that return the first element in queue and remove it
        '''
        if self.queue==[]:
            return None
        else:
            first = self.queue[-1]
            del self.queue[-1]
            return first
    def front(self):
        '''
        function that return the first element in queue
        '''
        if self.queue==[]:
            return None
        else:
            return self.queue[-1]
    def rear(self):
        '''
        function that return the last element in queue
        '''
        if self.queue==[]:
            return None
        else:
            return self.queue[0]
    def __len__(self):
        '''
        return the queue length
        '''
        return int(len(self.queue))
    def is_empty(self):
        '''
        return True if queue is empty else False
        '''
        return self.queue==[]
    def __repr__(self):
        '''
        repr overload
        '''
        copyqu = copy.deepcopy(self.queue)
        p=''
        for i in reversed(copyqu):
            p= p +str(i)+'\n'
        return p.strip()
    
class Department:
    '''
    This class represents department
    '''
    def __init__(self,name):
        '''
        Constructor
        '''
        self.name = name
        self.students_BST = Binary_search_tree()
        self.id2nodes = {}
    def insert(self,student):
        '''
        insert student to this department,if this student already in this department-make nothing
        return None
        '''
        #pok = Tree_node(Student.get_average(student),student)
        sid = str(student.student_id)
        self.id2nodes[sid]=Node(copy.copy(student))
        if isinstance(student, ForeignStudent):
            savg = ForeignStudent.get_average(student)
        else:
            savg = Student.get_average(student)
        self.students_BST.insert(savg,student)
        
    def delete_student_by_id(self,student_id):
        '''
        delete student from this Department
        '''
        stu = self.id2nodes.get(str(student_id),0)
        if stu==0:
            return
        stu_avg = stu.value.get_average()
        self.students_BST.delete(stu_avg)
        self.id2nodes.pop(str(student_id))
        
    def get_student_by_id(self,student_id):
        '''
        delete student from this Department
        '''
        if (str(student_id) in self.id2nodes.keys()):return True
        return False

    def get_student_by_id_or_none(self,student_id):
        '''
        delete student from this Department
        '''
        if (str(student_id) in self.id2nodes.keys()):return self.id2nodes.get(str(student_id)).value
        else:return Student('omar',999999909)


        
    def add_subject_by_student_id(self,student_id,subject):
        '''
        add subject to the student with the input student_id
        '''
        stu = self.id2nodes.get(str(student_id),0)
        if stu==0:
            return
        self.delete_student_by_id(student_id)
        the_stu = stu.value
        the_stu.add_subjects([subject])
        self.insert(the_stu)
        
    def warnings(self):
        '''
        return queue of the students that in this Department and under warning
        '''
        bad_stu_lst =[]#list of the students that under warning
        for i in self.id2nodes:
            stu = self.id2nodes[i].value
            if stu.is_warning()==True:
                bad_stu_lst.append(stu)
        bad_stu_lst = sorted(bad_stu_lst)
        warn = Queue()
        for fail in bad_stu_lst:#fill the warn queue
            warn.enqueue(fail)
        return warn
    
    def __repr__(self):
        '''
        repr overload
        '''
        strr = 'Department: '+self.name + '\n'
        inorder_lst = Binary_search_tree.inorder(self.students_BST)
        stu_lst=[]
        for i in inorder_lst:
            stu_lst.append(i[1])
        reg_stu =[]
        for_stu=[]
        for st in stu_lst:
            if isinstance(st, ForeignStudent):
                for_stu.append(st)
            else:
                reg_stu.append(st)
        st_dict={}
        for st in reg_stu:
            st_dict[st.get_average()]=st
        for st in for_stu:
            st_dict[st.get_average()]=st
        
        st_dict_to_lst = sorted(st_dict)
        #strr1 = (str(st_dict[m]) +'\n' for m in st_dict)
        strr1=''
        for m in range(len(st_dict_to_lst)-1):
            strr1 = strr1 + str(st_dict[st_dict_to_lst[m]]) +'\n'
        restr = strr+strr1+str(st_dict[st_dict_to_lst[-1]])+'\n'
        return restr
        