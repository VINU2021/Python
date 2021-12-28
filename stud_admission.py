--student admission--
import csv
def write_csv(info_list):
    with open('student_info.csv','w+',newline='')as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(["Name","Age","Contact number","Email.ID"])
        writer.writerow(info_list)
condn = True
while(condn):
    student_info=input("enter student information in the follwoing format(Name Age Contact_number Email_ID):")
    print("entered information:" + student_info)
    student_list=student_info.split(' ')
    print("entered splitup information:" + str(student_list))
    write_csv(student_list)
    check_condn=input("enter (yes/no) if you want to enter information for another student:")
    if check_condn=="yes":
        condn=True
    elif check_condn=="no":
        condn=False
