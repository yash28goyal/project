from prettytable import PrettyTable
import datetime
from PIL import Image
im = Image.open(r"C:\Users\yashg\OneDrive\Desktop\New folder\QRCODE.jpeg")

x = datetime.datetime.now()

print('--------------WELCOME TO COLLEGE RESTAURANT--------------\n')
table = PrettyTable(['Item Name', 'Item Price'])
total = 0 # without gst
grand_total = 0 # with gst
  
while(True):
    name = input('Enter Item name:')
      
    if(name != 'q'):
        price = int(input('Enter the Price:'))
          
        total += price
        grand_total = total + ((total)*(5/100)) 
        table.add_row([name, price])
        continue
      
    elif(name == 'q'):
        break
payment = 0

while (payment==0):
    print("Enter the mode !")
    print("""1) Cash""")
    print("""2) Credit/Debit Card""")
    print("""3) UPI""")
    n=int(input("Enter the payment method number : "))
    while (n>0):
        if (n == 1):
            print("your payment method is cash . please pay the bill",grand_total,'/-')
            break
        elif(n == 2):
            print("your payment method is Credit/Debit Card . please pay the bill",grand_total,'/-')
            input("CARD HOLDER NAME :")
            input("CARD NUMBER :")
            input("CVV : ")
            break
        elif(n==3):
            print("your payment method is UPI. please pay the bill.",grand_total,'/-')
            im.show()
            break
        else:
            print("Invalid Input")
            break
    break
table.add_row(['TOTAL', grand_total])
print(table)
print('Date and Time /-',x)
print('\nThanks for coming in College Restaraunt :)')
print('Your total bill amount is ', grand_total, '/-')
print('The Bill incudes 2.5% SGST and 2.5% CSGT ')
print('Total without GST ',total,'/-')
print("----------------------------------------------------------------------------------------------------------------")
ques = input("It would be great if you share your thoughts on food and service. (say yes or no ): ")
print("----------------------------------------------------------------------------------------------------------------")
g = " INVALID INPUT !!"
if ques == 'yes' :
    rvw = input("Share your Honest Review : ")
    print("----------------------------------------------------------------------------------------------------------------")
    star = input("RATE the FOOD and SERVICE from one to five stars !! (*) : ")
    for f in star:
        if f==('*') :
            print("Thanks for your honest review",':',star)
            break
        elif f==('**'):
            print("Thanks for your honest review",':',star)
            break
        elif f==('***'):
            print("Thanks for your honest review",':',star)
            break
        elif f==('***'):
            print("Thanks for your honest review",':',star)
            break
        elif f==('****'):
            print("Thanks for your honest review",':',star)
            break
        elif f==('*****'):
            print("Thanks for your honest review",':',star)
            break
        else :
            print(g)
            break
elif ques == "no":
    print("----------------------------------------------------------------------------------------------------------------")
else :
    print("INVALID INPUT !! ")
