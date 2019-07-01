import pandas as pd

File_Name = "SpecificAlertCheck_2019-6-11_1617.csv"
# List of Tuples
students = [ ('jack', 34, 'Sydeny' , 'Australia') ,
             ('Riti', 30, 'Delhi' , 'India' ) ,
             ('Vikas', 31, 'Mumbai' , 'India' ) ,
             ('Neelu', 32, 'Bangalore' , 'India' ) ,
             ('John', 16, 'New York' , 'US') ,
             ('Mike', 17, 'las vegas' , 'US')  ]
infile = open ( File_Name , 'r' )

dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City' , 'Country'], index=['a', 'b', 'c' , 'd' , 'e' , 'f'])
#print dfObj
for line in infile:
   linenew = line.split('\n')
   linenew2 = linenew[2]
   #if line[1]:
   #   print line
   print linenew2
   #exit(20)