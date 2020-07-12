import time
import os 
from app import Academy  
import pages
def main():

   
    while True:
        time.sleep(1)
        os.system('clear')
        print('Welcome To IT Academy')
        pages.page_1()
        option_page_1 = int(input('Choose the option above: '))
        options_switcher =  {
            1 : Academy().inquiry,
            2 : Academy().registration, 
            3 : Academy().print_student_info, 
            4 : Academy().update,
            5: Academy().delete_student,
        }
        options_switcher.get(option_page_1, 'Enter valid option')()
if __name__ =='__main__':
    main()