#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime


# In[2]:


class Car_Rental_Company:
    """
    Car_Rental_Office_Name: Name of the Car rental Company
    Office_Location: Address of the ar rental Company
    Phone_Number: Contact number
    Email_id: Email id of the Car rental Company
    """
    def __init__(self, Car_Rental_Office_Name = "ABC Car Rental", Office_Location = "Manchester" , 
                 Phone_Number = 1122112211, Email_id = "abcrental@abc.com"):
        self.Name = Car_Rental_Office_Name
        self.Location = Office_Location
        self.ContactNumber = Phone_Number
        self.ContactMail = Email_id 
        global Cars
        Cars = {"ECONOMY":10,"SUV":8,"COMPACT":15}  
        
    def display_Car_Rental_info(self):
        """
        Display Car Rental company Address and Contact information
        """
        print(f"*******Welcome to {self.Name} Car Rental Company*********")
        print(f"{self.Location}\n{self.ContactNumber}\n{self.ContactMail}")
        print()
    
    def display_cars(self):
        #Cars = {"ECONOMY":10,"SUV":8,"COMPACT":15}
        print("**********************Available Cars**********************")
        print("Car ID\tCar Type\tAvailability")
        print(f"1\tECONOMY\t\t{Cars.get('ECONOMY')}\n2\tSUV\t\t{Cars.get('SUV')}\n3\tCOMPACT\t\t{Cars.get('COMPACT')}")
        print("**Price Mode**\nHourly : $20\tDaily : $15\tWeekly : $10")
        print()
        
    
        


# In[3]:


custlist = {}
custdetail = {}
id = 1110


# In[4]:


class Customer:
    """
    Customer Class
    custname: Name of the customer
    address: Address of the customer
    phone_number: phone number of the customer
    emailid: email id of the customer
    driverid: driver id of the customer
    """
    def __init__(self):
        pass
      
    def get_user_details(self):
        """
        User will be asked to enter the details. if the values are invalid then exception message will be thrown.
        """
        while (True):
            try:
                self.Name = input("Enter Name : ")  
                self.Address = input("Enter Address : ") 
                self.Phone_Number = int(input("Enter Contact No : "))
                self.Email_Id =input("Enter Email Id : ") 
                self.Driver_Id = input("Enter Driver Id : ")    
                print()
            except ValueError:
                print ("Invalid values. Enter the correct values.")
                print()
            else:
                return
    
    def display_customer_info(self): #public method of the Customer class
        """
        Customer billing information will be displayed
        """
        print("************CUSTOMER INFORMATION**********************")
        print(f"Customer Name: {n1}\nAddress: {n2}\nPhone Number: {n3}\nEmail: {n4}\nDriver Id: {n5}")
        print()


# In[5]:


class Booking(Car_Rental_Company):
    """
    Once customer confirm booking. Inventory will be updated accordingly.
    """
    
    def __init__(self, cust):
    
        super(Booking,self).__init__()
        self.Customer = cust  
        
    def get_user_action(self):
        while (True):
            self.User_Action = int(input("Would you like to rent or return the car\nEnter 1-Rent or 2-Return or 3-Exit : ")) 
            print()
            if self.User_Action == 1:
                print("Thank you! for choosing the service")
                print()
                self.Customer.get_user_details()
                self.get_pickup_datetime()
                self.Car_pickup()
                global id
                global custlist
                custlist.update({id:[self.User_Action,self.Customer.Driver_Id,self.car_type1,self.No_of_Cars1,self.mode,self.dt1]})
                print("**Receipt Created**") 
                print(f"Receipt ID : {id}\nCar ID : {self.car_type1}\nNo of Cars : {self.No_of_Cars1}\nPrice Mode : {self.mode}\nPickup DateTime : {self.dt1}")
                print()
                global custdetail          
                custdetail.update({id:[self.Customer.Name,self.Customer.Address,self.Customer.Phone_Number,self.Customer.Email_Id,self.Customer.Driver_Id]})
                print("**Checking for Inventory Update**")
                print()
                self.display_cars()
                id=id+10
            elif self.User_Action == 2:
                try:
                    self.receipt_id = int(input("Enter Receipt ID to return car : "))
                    print()
                    if (self.receipt_id in custlist):
                        print("Thank you! for using the service")
                        print()
                        self.get_return_datetime()
                        global ct
                        global cn
                        global dt
                        global pm
                        ct = custlist.get(self.receipt_id)[2]
                        cn = custlist.get(self.receipt_id)[3]
                        dt = custlist.get(self.receipt_id)[-1]
                        pm = custlist.get(self.receipt_id)[-2]
                        global n1
                        global n2
                        global n3
                        global n4
                        global n5
                        n1 = custdetail.get(self.receipt_id)[0]
                        n2 = custdetail.get(self.receipt_id)[1]
                        n3 = custdetail.get(self.receipt_id)[2]
                        n4 = custdetail.get(self.receipt_id)[3]
                        n5 = custdetail.get(self.receipt_id)[4]
                            
                        if (self.car_type2 == ct):
                            if (self.No_of_Cars2 <= cn):
                                print ("**Receipt ID updated**")
                                print()
                                global nc
                                nc = cn - self.No_of_Cars2
                                custlist.update({self.receipt_id:[self.User_Action,self.Customer.Driver_Id,self.car_type2,nc,self.mode,self.dt2]})
                                print(f"Receipt ID : {self.receipt_id}\nCar ID : {self.car_type2}\nNo of Cars : {nc}\nDrop Datetime : {self.dt2}")
                                print()
                                self.Car_drop()
                                print("**Bill generated**")
                                print()
                                self.billing()
                                print("**Checking for Inventory Update**")
                                print()
                                self.display_cars()

                                self.display_bill()
                            elif (self.No_of_Cars2 > cn):
                                print("Trying to return More number of cars than booked")
                                print()
                                continue
                            elif (self.No_of_Cars2 == 0):
                                print("Car Returned already. NO car pending to return")
                                print()
                                continue
                        else:
                            print(f"Car Type: {self.car_type2} is not booked under the Receipt ID : {self.receipt_id}")
                            print()
                            continue
                           
                    else:
                        print("Invalid Receipt ID")
                        print()
                        continue
                except ValueError:
                    print ("Invalid Receipt ID")
                    print()
                else:
                    return            
            elif self.User_Action == 3:
                return

            else:
                print ("Not a valid entry")
                print()
        
    def get_pickup_datetime(self):
        while (True):
            try:
                self.date1 = input("Enter pickup date in YYYY-MM-DD format : ")
                year, month, day = map(int, self.date1.split('-'))
                self.date1 = datetime.date(year, month, day)
                self.time1 = input("Enter pickup time in HH:MM:SS format : ")
                print()
                hour, minute, second = map(int, self.time1.split(':'))
                self.time1 = datetime.time(hour, minute, second)
                global dt1
                self.dt1 = datetime.datetime(self.date1.year, self.date1.month, self.date1.day, self.time1.hour,
                                             self.time1.minute, self.time1.second)
                print(f"Pickup date and time is : {self.dt1}")
                print()
                return self.dt1
            except ValueError:
                print("Invalid Date and Time. Please enter correct values")
                print()
            else:
                return

    def Car_pickup(self):
        while (True):
            try:
                self.mode = int(input("Enter Price Mode: \nHourly = 1\nDaily = 2\nWeekly = 3 : "))
                if self.mode <=3:
                    self.car_type1 = int(input("Enter the Car ID (1\\2\\3) :"))
                    if self.car_type1 <=3:
                        self.No_of_Cars1 = int(input("Enter the number of cars for pickup : "))
                        print()
                        if self.car_type1 == 1:
                            if Cars.get('ECONOMY') >= self.No_of_Cars1:
                                temp = Cars.get('ECONOMY') - self.No_of_Cars1
                                Cars.update({"ECONOMY":temp})
                            else:
                                print("Cars requested is not available")
                                print()
                                return
                        elif self.car_type1 == 2:
                            if Cars.get('SUV') >= self.No_of_Cars1:
                                temp = Cars.get('SUV') - self.No_of_Cars1
                                Cars.update({"SUV":temp})
                            else:
                                print("Cars requested is not available")
                                print()
                                return
                        elif self.car_type1 == 3:
                            if Cars.get('COMPACT') >= self.No_of_Cars1:
                                temp = Cars.get('COMPACT') - self.No_of_Cars1
                                Cars.update({"COMPACT":temp})
                            else:
                                print("Cars requested is not available")
                                print()
                                return
                        else:
                            print("Invalid Car ID entered")
                            print()
                            return self.car_type1
                    else:
                        print("Invalid Car ID entered")
                        print()
                        continue
                    print("Car booked succesfully")
                    print()
                else:
                    print("Invalid Price Mode. Please enter 1/2/3")
                    print()
                    continue
            except ValueError:
                print("Invalid Entry. Please enter correct values")
                print()
            else:
                return
            
    
    def get_return_datetime(self):
        while (True):
            try:
                self.car_type2 = int(input("Enter the Car ID (1\\2\\3) :"))
                self.No_of_Cars2 = int(input("Enter the number of cars for drop : "))
                self.date2 = input("Enter return date in YYYY-MM-DD format : ")
                year, month, day = map(int, self.date2.split('-'))
                self.date2 = datetime.date(year, month, day)
                self.time2 = input("Enter return time in HH:MM:SS format")
                print()
                hour, minute, second = map(int, self.time2.split(':'))
                self.time2 = datetime.time(hour, minute, second)
                global dt2
                self.dt2 = datetime.datetime(self.date2.year, self.date2.month, self.date2.day, self.time2.hour,
                                             self.time2.minute, self.time2.second)
                print(f"Return date and time is : {self.dt2}")
                print()
                return self.dt2
            except ValueError:
                print("Invalid Date and Time. Please enter correct values")
                print()
            else:
                return
    def Car_drop(self):
        #self.car_type2 = input("Enter the Car ID (1\\2\\3) :")
        #self.No_of_Cars2 = int(input("Enter the number of cars for drop : "))
        if (self.car_type2 == ct):
            if self.car_type2 == 1:
                temp = Cars.get('ECONOMY') + self.No_of_Cars2
                Cars.update({"ECONOMY":temp})
            elif self.car_type2 == 2:
                temp = Cars.get('SUV') + self.No_of_Cars2
                Cars.update({"SUV":temp})
            elif self.car_type2 == 3:
                temp = Cars.get('COMPACT') + self.No_of_Cars2
                Cars.update({"COMPACT":temp})
            else:
                print("Invalid Car ID entered")
                print()
                return
            print("Car returned succesfully")
            print()
        
    def billing(self):
        if (self.car_type2 == ct):
            if (self.No_of_Cars2 <= cn):
                if self.No_of_Cars2 >= 1:
                    self.diff = self.dt2 - dt
                    self.weeks = int(self.diff.days/7)
                    self.hours = int(self.diff.total_seconds()/(60*60))
                    try:
                        #self.mode = input("Enter Price Mode: \nHourly = 1\nDaily = 2\nWeekly = 3 : ")
                        if pm == 1:
                            if self.diff.days <= 0:
                                self.price = self.hours*20
                            else:
                                self.price = self.diff.days*15
                        elif pm == 2:
                            if self.weeks>=7:
                                self.price = self.diff.days*10
                            else:
                                self.price = self.diff.days*15
                        elif pm == 3:
                            self.price = self.diff.days*10 
                        else:
                            print ("Invalid Price Mode entered")
                            print()
                            return
                        print(f"The billing amount calculated : ${self.price}")
                        print()
                    except ValueError:
                        print("Invalid entry")
                        print()
                    else:
                        return
                else:
                    print("NO Cars are booked")
                    print()
            else:
                print("No cars are pending to return and bill")
        else:
            print("Receipt ID don't have any car of the given ID")

    def display_bill(self):
        print("*****************************Bill****************************")
        print(f"*******Thankyou from {self.Name} Car Rental Company*********")
        print(f"\t\t\t\t\t{self.Location}\n\t\t\t\t\t{self.ContactNumber}\n\t\t\t\t\t{self.ContactMail}")
        print()
        print("*****Customer Details*****")
        self.Customer.display_customer_info()
        print()
        print(f"Pickup date and time is : {dt}")
        print(f"Return date and time is : {self.dt2}")
        print()
        print(f"No of Cars Returned : {self.No_of_Cars2}\n Car ID : {self.car_type2}")
        print()
        print(f"Rental Period: {self.diff}\nRented Weeks : {self.weeks}\nRented Days : {self.diff.days}        \nRented Hours : {self.hours}\nPrice Mode : {pm}")
        print()
        print(f"The billing amount for 1 car is: ${self.price}")
        print(f"Total Bill amount {self.No_of_Cars2} * {self.price} is : {self.No_of_Cars2*self.price}")
        print()
        
        
              

