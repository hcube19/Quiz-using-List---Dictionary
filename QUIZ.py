#Store questions and answer in a list in the form
# [[question 1, answer 1],[question 2, answer 2],.......]

questions=[["""1. Which of the following methods can be used to find the
largest and smallest number in a linked list?
a) Recursion
b) Iteration
c) Both Recursion and iteration #
d) Impossible to find the largest and smallest numbers""","c"],
["""2. Process of inserting an element in stack is called ____________
a) Create
b) Push#
c) Evaluation
d) Pop""","b"],
["""3. Which of these best describes an array?
a) A data structure that shows a hierarchical behavior
b) Container of objects of similar types#
c) Arrays are immutable once initialised
d) Array is not a data structure""","b"],
["""4. How do you initialize an array in C?
a) int arr[3] = (1,2,3);
b) int arr(3) = {1,2,3};
c) int arr[3] = {1,2,3};#
d) int arr(3) = (1,2,3);""","c"],
["""5. How do you instantiate an array in Java?
a) int arr[] = new int(3);
b) int arr[];
c) int arr[] = new int[3];#
d) int arr() = new int(3);""","c"],
["""6. Which of the following is the correct way to declare a multidimensional
array in Java?
a) int[] arr;
b) int arr[[]];
c) int[][]arr;#
d) int[[]] arr;""","c"],
["""7. When does the ArrayIndexOutOfBoundsException occur?
a) Compile-time
b) Run-time#
c) Not an error
d) Not an exception at all""","b"],
["""8. Which of the following concepts make extensive use of arrays?
a) Binary trees
b) Scheduling of processes
c) Caching
d) Spatial locality#""","d"],
["""9. What are the advantages of arrays?
a) Objects of mixed data types can be stored
b) Elements in an array cannot be sorted
c) Index of first element of an array is 1
d) Easier to store elements of same data type#""","d"],
["""10. Courses in IIITMK?
a) Machine Intelligence
b) Data Analytics
c) Geospatial Analytics
d) Cyber Security""","abcd"],
["""11. Assuming int is of 4bytes, what is the size of int arr[15];?
a) 15
b) 19
c) 11
d) 60#""","d"],
["""12. In general, the index of the first element in an array is __________
a) 0#
b) -1
c) 2
d) 1""","a"],
["""13. Elements in an array are accessed _____________
a) randomly#
b) sequentially
c) exponentially
d) logarithmically""","a"],
["""14. Process of removing an element from stack is called __________
a) Create
b) Push
c) Evaluation
d) Pop#""","d"],
["""15. In a stack, if a user tries to remove an element from an empty stack
it is called _________
a) Underflow#
b) Empty collection
c) Overflowd) Garbage Collection""","a"],
["""16. The data structure required to check whether an expression contains a
balanced parenthesis is?
a) Stack#
b) Queue
c) Array
d) Tree""","a"],
["""17. What data structure would you mostly likely see in non recursive
implementation of a recursive algorithm?
a) Linked List
b) Stack#
c) Queue
d) Tree""","b"],
["""18. The process of accessing data stored in a serial access memory is
similar to manipulating data on a ________
a) Heap
b) Binary Tree
c) Array
d) Stack#""","d"],
["""19. Which data structure is needed to convert infix notation to postfix
notation?
a) Branch
b) Tree
c) Queue
d) Stack#""","d"],
["""20. The prefix form of an infix expression (p + q) – (r * t) is?
a) + pq – *rt
b) – +pqr * t
c) – +pq * rt#
d) – + * pqrt""","c"]
]

print(""" The questions are categorised into 5 topics.All the questions are
multiple choice questions (MCQ) type, with possibly more than one correct
answer.""")
print(""" ####Instructions :###
*.If question has multiple correct answer,enter both option without space or
comma between them. for eg. "bc" (without quotes)if option b and c are
correct.
*.To SKIP a question just PRESS ENTER,Skipped questions will be shown at the
end.
""")

from heapq import heappop, heappush
pos=1
neg=0.5
count=0

#Dividing questions into sections
section1=int(10/20*len(questions))
section2=int(section1+4/20*len(questions))
section3=int(section2+3/20*len(questions))
section4=int(section3+2/20*len(questions))
section5=len(questions)
sections=[0,section1,section2,section3,section4,section5]

total=int(input("Enter the number of Students: "))
record={}

#You can remove this for loop, if only you want to give the quiz.
for student in range(total):
    name=input("Enter the name")
    no_neg = 0
    correct = 0
    wrong = 0
    key=0
    skip=[]      #will hold all the index of not answered questions in first run
    score=0

    neg_score=0
    # NOTE : my marking scheme is bit harsh. everytime u answer wrong it will be penalized by n times.
    # Eg. - first wrong =  - 1x0.5, second wrong = - ( first wrong + 2 x 0.5  )... so on
    # If u want to penalize 0.5 for every time then do :
    # 1. remove **neg_score**
    # in the end change **score=correct*pos-neg_score** to score=correct*(-wrong*0.5)
    
    part = ["1.section1", "2.section2", "3.section3", "4.section4", "5.section5"]
    print(part)
    while key!=5:
        section=int(input("Enter the section NUMBER : "))
        while part[section-1]=="Done":
            print("Section already Completed. Select other section")
            section = int(input("Enter the section NUMBER : "))
        part[section-1]="Done"
        key=key+1
        for question in range(sections[section-1],sections[section]):
            print(questions[question][0])
            answer=input("Enter the Option/s : ")
            if answer==questions[question][1]:
                correct=correct+1
            else:
                if answer=="" or None:
                    skip.append(question)
                    question=question+1
                else:
                    wrong=wrong+1
                    neg_score=neg_score+neg*wrong
        print(part)
    if len(skip)!=0:
        print()
        print("Following questions are left")
        print()
        for question in range(len(skip)):
            print(questions[skip[question]][0])
            answer=input("Enter the Option/s : ")
            if answer==questions[skip[question]][1]:
                correct=correct+1
            else:
                if answer=="" or None:
                    no_neg=no_neg+1
                else:
                    wrong=wrong+1
                    neg_score=neg_score+neg*wrong
    print("Correct answers: ",correct)
    print("Wrong answers: ",wrong)
    print("Questions Not Attempted",no_neg)
    score=correct*pos-neg_score
    print("Score of ",name," : ",score)
    record[score]=name
print("Records of Student Score : ",record)
key=record.keys()
heap = []
for ele in key:
    heappush(heap, ele)
sort = []
while heap:
    sort.append(heappop(heap))
sort=reversed(sort)
rank={}
count=0
for key in sort:
    count=count+1
    rank[count]=[record[key],key]
print("Ranking Of Students are : :", rank)