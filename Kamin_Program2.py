#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 02:43:40 2020

@author: jkenglish
"""

#Create an Employee class

class Employee:
    
    #Employee name and number are the attributes.
    
    def __init__ (self):
        
        self.Employee_name = ''
        
        self.Employee_number = 0
    

    #Mutator for Employee name
    
    def set_Employee_name(self,Employee_name):
        
        self.Employee_name = Employee_name
        
    #Accessor for Employee name
    def get_Employee_name(self):
         
        return (self.Employee_name)
    #Mutator for Employee
    
    def set_Employee_number(self, Employee_number):
        
        self.Employee_number = Employee_number

    #Accessor for Employee     
        
    def get_Employee_number(self):
        
        return (self.Employee_number)

    
class Productionworker(Employee):
    
     #Initialize attributes of the parent class
    
     def __init__(self):
         
         Employee.__init__(self)
    
     #Mutator for shift number
     def set_shiftnumber(self,shiftnumber):
         
         self.shiftnumber = shiftnumber
  
    
     #Accessor for shift number
   
     def get_shiftnumber(self): 
         
         return (self.shiftnumber)
    
     #Mutator for hourly pay rate
        
     def set_Hourly_Payrate(self,Hourly_Payrate):
        
         self.Hourly_Payrate = Hourly_Payrate
   
     #Accessor for hourly pay rate
    
     def get_Hourly_Payrate(self):
         
         return (self.Hourly_Payrate)


#Program that creates an object of the Productionworker class


def main():      
 
  #Get employee details as user input
  
  print("\nWelcome to the Employee class!\n")  
  
  employee_name = input("Enter the name of the employee: ")
  
  employee_number = int(input("Enter the employee number: "))
  
  Shiftnumber = int(input("Enter the shift number: "))
  
  Hourly_Payrate = int(input("Enter the hourly pay rate: "))
  
  #Create an instance of the Employee class
  
  #Call the mutator and accessor methods
  
  employee = Employee()
  
  employee.set_Employee_name(employee_name)
  
  employee.set_Employee_number(employee_number)
  
  employeename = employee.get_Employee_name()
  
  employeenumber = employee.get_Employee_number()
  
  #Create an instance of the Productionworker class

  #Call the mutator and accessor methods
  
  #Determine shift type based on user input for shift number
  
  production_worker = Productionworker()
  
  production_worker.set_shiftnumber(Shiftnumber)
  
  shift_type = production_worker.get_shiftnumber()
  
  if shift_type == 1:
      
       shift = "Day Shift"
  
  elif shift_type == 2:
      
       shift = "Night Shift"
  
  production_worker.set_Hourly_Payrate(Hourly_Payrate)
  
  pay = production_worker.get_Hourly_Payrate()
  
  print(f"\nEmployee name: {employeename}, Employee number: {employeenumber}, Shift type: {shift}, Pay rate: {pay}  ")
  

main()  
  
  
