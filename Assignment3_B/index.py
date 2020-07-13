import csv
class manangement():

  print("""
  1. To view courses
  2. To see list of Students
  3. To add new student
  4. To cancel student enroll
  5. To update the installment
  6. To return the installment who have successfully complete course



  """)
  select=int(input("Enter the Number: "))
  if select==1:
    with open('course.csv','r') as file:
      reader=csv.reader(file)
      for i in reader:
        print("{}".format(i))
        
      

  if select==2:
    with open('dict.csv','r') as file:
      reader=csv.reader(file)
      for i in reader:
        print(" {} {}".format(i[0],i[1]))
    
    

  if select==3:
    name=(input('Enter the name of New student: '))
    fee=int(input('Enter the fee: '))
    data=[name, fee]
    with open('dict.csv','a+') as file:
      write= csv.writer(file)
      write.writerow(data)

  if select==4:
    lines = list()
    members= input("Please enter a member's name to be deleted:")

    with open('dict.csv', 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:


          lines.append(row)
        

          for field in row:
            if field == members:


              lines.remove(row)

    with open('dict.csv', 'w') as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(lines)

  if select==5:
    installment=input("Enter the name of Student if he/she pay second assignment: ")
    amount=int(input("Enter the amount: "))
    lines = list()


    with open('dict.csv', 'r') as readFile:
      reader = csv.reader(readFile)

      for row in reader:
        lines.append(row)
        for field in row:
          if field==installment:
            row[1]=int(row[1])+amount
    with open('dict.csv', 'w') as writeFile:

      writer = csv.writer(writeFile)

      writer.writerows(lines)

  if select==6:
    installment=input("Enter the name of Student who successfully completed course: ")
    lines = list()


    with open('dict.csv', 'r') as readFile:
      reader = csv.reader(readFile)

      for row in reader:

        lines.append(row)
        for field in row:

          if field==installment:
            row[1]=int(row[1])-2000
    with open('dict.csv', 'w') as writeFile:

      writer = csv.writer(writeFile)

      writer.writerows(lines)


stud= manangement
stud

