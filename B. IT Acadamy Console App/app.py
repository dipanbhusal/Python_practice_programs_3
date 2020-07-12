import os 
import time 
import csv 

class Academy:
    def __init__(self):
        self.headers = ['Name', 'Course Enrolled', 'Payment Status', 'Remaining Amount', 'Contact']

    def inquiry(self):
        with open('course.csv') as file:
            csv_reader = csv.DictReader(file)
            self.course_detail = {}
            
            for row in csv_reader:
                course_sn = {}
                self.course_detail[row['S.N']] = course_sn   
                course_sn['Course'] = row['Course']
                course_sn['Duration'] = row['Duration']
            print('These are the available courses: ')
            print('S.N\tCourse\t\t\tDuration Of Course(Months)')
            for key, value in self.course_detail.items():
                
                print('{:8s}{:24s}{}'.format(key,value["Course"],value["Duration"]))
    def registration(self):
        name_of_student = input('Enter your name: ')
        contact_number = input('Enter your contact number: ')
        self.inquiry()
        course_option = input('Enter the S.N. of course you want to be enrolled among above available courses: ')
        course = self.course_detail[course_option]['Course']
        payment_option = input('Write F for full payment or I for installment payment: ')
        remained_fee = 0
        if payment_option == 'I':
            payment_status = 'Installment'
            remained_fee = 10000
        elif payment_option =='F':
            payment_status = 'Fully Paid'
        else:
            print('Please enter valid option.')
        self.headers = ['Name', 'Course Enrolled', 'Payment Status', 'Remaining Amount', 'Contact']
        infos = [name_of_student.capitalize(),course,payment_status, remained_fee,contact_number]
        file_name = 'student-info.csv'
        file_isExist = os.path.isfile(file_name)
        with open(file_name, 'a') as file:
            writer = csv.writer(file)
            if not file_isExist:
                writer.writerow(self.headers)
            writer.writerow(infos)
        print('You are enrolled in course successfully.Going to main menu.')
        time.sleep(2)
    def student_information(self):
        with open('student-info.csv','r') as file:
            reader = csv.DictReader(file)
            self.students_info = {}
            # headers = ['Name', 'Course Enrolled', 'Payment Status', 'Remaining Amount', 'Contact']
            for rows in reader:
                student_info = {}

                self.students_info[rows['Name']] = student_info
                student_info[self.headers[0]] = rows['Name']
                student_info[self.headers[1]] = rows['Course Enrolled']
                student_info[self.headers[2]] = rows['Payment Status']
                student_info[self.headers[3]] = rows['Remaining Amount']
                student_info[self.headers[4]] = rows['Contact']
            return self.students_info
    def print_student_info(self): 
        info = self.student_information() 
        print(f'{self.headers[0]}\t\t{self.headers[1]}\t\t{self.headers[2]}\t\t{self.headers[3]}\t{self.headers[4]}')
        for key, value in info.items():
            print('{:16s}{:24s}{:24s}{:24s}{}'.format(value['Name'],value['Course Enrolled'],value['Payment Status'],value['Remaining Amount'],value['Contact']))
        input('Press Enter to return to main menu...')
    def update(self):
        name  = input('Enter your name: ').capitalize()
        student_info = self.get_student_info_dict(name)
        remaining_amount = int(student_info[name]['Remaining Amount'])
        print(f'The remaining balance for {student_info[name]["Name"]} = {remaining_amount}')
        time.sleep(1)
        if remaining_amount != 0:
            try:
                student_info[name]['Payment Status'] = 'Fully Paid'
                student_info[name]['Remaining Amount'] = 0
                print('Information updated successfully')
            except KeyError:
                print('Enter the valid name.')
            self.csv_operation('student-info.csv','write',student_info)
        else:
            print('You have already paid full amount. ')
        time.sleep(1)
    def delete_student(self):
        name = input('Enter your name: ').capitalize()
        student_info = self.get_student_info_dict(name)
        student_info.pop(name)
        
        self.csv_operation('student-info.csv','write',student_info)
        
        print('You have successfully left the course. Returning to main menu ')
        time.sleep(2)
    def get_student_info_dict(self,name):
        student_info = self.student_information()
        
        try:
            print(f'Student found for name {student_info[name]["Name"]}')
            time.sleep(1)
            return student_info
        except KeyError:
            print('Student name not found. Enter the valid name.')
        
    def csv_operation(self,filename,operation, dic_file):
        if operation == 'write':
            with open(filename, 'w') as file:
                writer =  csv.DictWriter(file, fieldnames= self.headers)
                writer.writeheader()
                for key, values in dic_file.items():
                    writer.writerow(values) 
    

