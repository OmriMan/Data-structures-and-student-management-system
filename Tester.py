from hw8 import Subject, Student, ForeignStudent, Queue, Department
big_test_list=[]
bool_list=[]
#print(Subject('Algebra',95.0,4.5))
uriel=Student('Uriel',654321)
#print(uriel)
#print(str(uriel)=="Student Uriel[654321], avg:0.0, points:0.0, grades:no subjects yet.")
bool_list.append(str(uriel)=="Student Uriel[654321], avg:0.0, points:0.0, grades:no subjects yet.")
###
uriel.add_subjects([Subject('Algebra',93.0,4.5),Subject('Python',95.0,4.0),Subject('SQL',45.,2.0)])
#print(uriel)
uriel.add_subjects([Subject('Algebra',93,4.5),Subject('Python',95,4),Subject('SQL',45,2)])
#print(uriel)
#print(str(uriel)=="Student Uriel[654321], avg:84.61904761904762, points:8.5, grades:SQL(2.0)-45.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
###
bool_list.append(str(uriel)=="Student Uriel[654321], avg:84.61904761904762, points:8.5, grades:SQL(2.0)-45.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
uriel.add_subjects([Subject('SQL',56.0,2.0)])
#print(uriel)
#print(str(uriel)=="Student Uriel[654321], avg:86.71428571428571, points:10.5, grades:SQL(2.0)-56.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
###
bool_list.append(str(uriel)=="Student Uriel[654321], avg:86.71428571428571, points:10.5, grades:SQL(2.0)-56.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
uriel.add_subjects([Subject('SQL',30.0,2.5)])
#print(uriel)
#print(str(uriel)=="Student Uriel[654321], avg:79.4090909090909, points:8.5, grades:SQL(2.5)-30.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
###
bool_list.append(str(uriel)=="Student Uriel[654321], avg:79.4090909090909, points:8.5, grades:SQL(2.5)-30.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
#print(uriel.is_warning(),"=?False")
bool_list.append(False) if uriel.is_warning() else bool_list.append(True)
ariel=ForeignStudent('Ariel',132456)
#print(ariel)
#print(str(ariel)=="ForeignStudent Ariel[132456], avg:0.0, points:0.0, grades:no subjects yet.")
###
bool_list.append(str(ariel)=="ForeignStudent Ariel[132456], avg:0.0, points:0.0, grades:no subjects yet.")
ariel.add_subjects([Subject('Algebra',93.0,4.5),Subject('Python',95.,4.0),Subject('SQL',45.,2.0)])
#print(ariel)
#print(str(ariel)=="ForeignStudent Ariel[132456], avg:89.80952380952381, points:8.5, grades:SQL(2.0)-45.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
###
bool_list.append(str(ariel)=="ForeignStudent Ariel[132456], avg:89.80952380952381, points:8.5, grades:SQL(2.0)-45.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
ariel.add_subjects([Subject('SQL',56.,2.0)])
#print(ariel)
#print(str(ariel)=="ForeignStudent Ariel[132456], avg:90.85714285714286, points:10.5, grades:SQL(2.0)-56.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
###
bool_list.append(str(ariel)=="ForeignStudent Ariel[132456], avg:90.85714285714286, points:10.5, grades:SQL(2.0)-56.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
ariel.add_subjects([Subject('SQL',30.0,2.5)])
#print(ariel)
#print(str(ariel)=="ForeignStudent Ariel[132456], avg:87.20454545454545, points:8.5, grades:SQL(2.5)-30.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
###
bool_list.append(str(ariel)=="ForeignStudent Ariel[132456], avg:87.20454545454545, points:8.5, grades:SQL(2.5)-30.0, Python(4.0)-95.0, Algebra(4.5)-93.0.")
#print(uriel.is_warning(),"=?False")
###
bool_list.append(False) if uriel.is_warning() else bool_list.append(True)

big_test_list.append((True,"Student")) if all(bool_list) else big_test_list.append((False,"Student"))

test_count = len(bool_list)
fail_count = test_count - sum(bool_list)
bool_list=[]

##################print("operator check:")
#print(ariel > uriel,"=?True")
###
bool_list.append(ariel > uriel)
#print(ariel >= uriel,"=?True")
###
bool_list.append(ariel >= uriel)
#print(ariel < uriel,"=?False")
###
bool_list.append(False) if ariel < uriel else bool_list.append(True)

#print(ariel > uriel,"=?True")
###
bool_list.append(ariel > uriel)
#print(ariel == uriel,"=?False")
###
bool_list.append(False) if ariel == uriel else bool_list.append(True)
#print(ariel != uriel,"=?True")
###
bool_list.append(ariel != uriel)

big_test_list.append((True,"operator check")) if all(bool_list) else print("---fail---/nfail : operator check")

test_count += len(bool_list)
fail_count += len(bool_list) - sum(bool_list)

bool_list=[]

#print("-----Queue-----")
q=Queue()
###
bool_list.append(len(q)==0)
###
bool_list.append(q.is_empty())
###
bool_list.append(q.rear()==None)
###
bool_list.append(q.front()==None)
q.enqueue(3)
###
bool_list.append(q.front()==3)
q.enqueue(4)
###
bool_list.append(q.rear()==4)
q.enqueue(5.5)
###
bool_list.append(q.rear()==5.5 and q.front()==3)


###
bool_list.append(len(q)==3)
###
bool_list.append(q.is_empty()==False)
###
bool_list.append(q.dequeue()==3)
###
bool_list.append(q.front()==4)
###
bool_list.append(q.dequeue()==4)
###
bool_list.append(q.dequeue()==5.5)
###
bool_list.append(q.dequeue()==None)
###
bool_list.append(q.is_empty())

big_test_list.append((True,"Queue")) if all(bool_list) else big_test_list.append((False,"Queue"))

test_count += len(bool_list)
fail_count += len(bool_list) - sum(bool_list)

bool_list=[]

#print("----department------")

hapaytana=Department('Hapaytana')

###
bool_list.append(hapaytana.name=='Hapaytana')
hapaytana.insert(uriel)
###
bool_list.append(hapaytana.get_student_by_id(654321))

hapaytana.insert(ariel)
###
bool_list.append(hapaytana.get_student_by_id(132456))

hapaytana.delete_student_by_id(132456)
###
bool_list.append(False) if hapaytana.get_student_by_id(132456) else bool_list.append(True)


hapaytana.delete_student_by_id(654321)
###
bool_list.append(False) if hapaytana.get_student_by_id(654321) else bool_list.append(True)

uriel=Student('Uriel',654321)
uriel.add_subjects([Subject('Algebra',60,4.5),Subject('Python',70,4),Subject('SQL',80,2)])
ariel=ForeignStudent('Ariel',132456)
ariel.add_subjects([Subject('Algebra',50.0,4.5),Subject('Python',60.0,4.0),Subject('SQL',70,2)])
assaf=ForeignStudent('Assaf',1212)
assaf.add_subjects([Subject('Algebra',20,4.5),Subject('Python',30,4),Subject('SQL',45,2)])
shay=Student('Shay',909)
shay.add_subjects([Subject('Algebra',10,4.5),Subject('Python',20,4),Subject('SQL',30,2)])
hapaytana.insert(uriel)
hapaytana.insert(ariel)
###
bool_list.append(hapaytana.get_student_by_id(132456))
bool_list.append(hapaytana.get_student_by_id(654321))

hapaytana.add_subject_by_student_id(132456,Subject('Snooker',100.0,5.0))
###
bool_list.append(True) if ('Snooker' in hapaytana.get_student_by_id_or_none(132456).get_subjects_names()) else bool_list.append(False)

hapaytana.insert(assaf)
###
bool_list.append(hapaytana.get_student_by_id(1212))
hapaytana.insert(shay)
###
bool_list.append(hapaytana.get_student_by_id(909))

big_test_list.append((True,"department")) if all(bool_list) else big_test_list.append((False,"department"))

test_count += len(bool_list)
fail_count += len(bool_list) - sum(bool_list)

print("number of tests : ",test_count)
print("Success :",test_count - fail_count)
for i in big_test_list:
    if i[0]!=True : print("need to fix :",i[1] ,"\n")
    
