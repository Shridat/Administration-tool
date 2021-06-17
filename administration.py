import csv
num=1
def write_csv(info_list):
    with open('C:/Users/Shrinivas/Desktop/student.csv' , 'a', newline='') as f:
        writer=csv.writer(f)
        if(f.tell()==0):
            writer.writerow(["Name","Age","Contact","E-mail ID"])
        writer.writerow(info_list)
    
condition=True
while(condition):
    student_info=input("Enter student information for student #{} in following manner(Name Age Phone Email):=".format(num))
    print("Entered information:"+student_info)
    info_list=student_info.split(" ")
    print("Entered Information list:"+str(info_list))
    print("\n The entered information is=\nName:{}\nAge:{}\nContact:{}\nEmail:{}".format(info_list[0],info_list[1],info_list[2],info_list[3]))
    choice=input("Is entered information is right?? type yes/no:")
    if choice=="yes":
        write_csv(info_list)
        condition_check=str(input("Do you want to enter information?type yes/no:"))
        if(condition_check=="yes"):
            condition=True
            num=num+1
        else:
            condition=False
    elif choice=="no":
        print("Plz reenter choice value??")
    
    
