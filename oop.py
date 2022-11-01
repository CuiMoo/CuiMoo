
class Officer:
    def __init__(self,name,surname,sal):
        self.name = name
        self.surname = surname
        self.__salary = sal

    def display(self):
        print(f'\nName : {self.name} {self.surname}')
        print(f'Full salary: {self.__salary}')

    def getSalary(self):
        print(f'latest salary :{self.__salary}')
    
    def setSalary(self,dept,sal):
        if dept == 'IT':
            if int(sal) > 5000:
                print('is unable to fix the new salary,Take the old data')
            else:
                self.__salary = sal
        else:
            self.__salary = sal
myname = input('Please insert name: ')
mysurname = input('Please insert surname :')
mydept = input('Please insert dept: ')
oldsal = input('Please insert old salary: ')
newsal = input('Please insert new salary: ')
ofc =Officer(myname,mysurname,oldsal)
ofc.display()
ofc.setSalary(mydept,newsal)
ofc.getSalary()
