class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property 
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
    @property 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
emp1 = Employee('Anh', 'Dung')
# print(emp1.email)
# print(emp1.fullname)

emp1.fullname = 'Minatozaki Sana'
print(emp1.first)
print(emp1.email)

del emp1.fullname
