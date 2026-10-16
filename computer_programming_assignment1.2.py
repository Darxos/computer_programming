name=input('your name')
has_student_id=input("do you have a student id ( yes/no)")
order_time=int(input("please enter the time hour in 24-hour format"))
dish1=input("enter 1st dish name")
dish2=input("enter 2nd dish name")
dish3=input("enter 3rd dish name")
d1price=int(input("enter 1st dish price"))
d2price=int(input("enter 2nd dish price"))
d3price=int(input("enter 3rd dish price"))
d1quantity=int(input("enter 1st dish quantity"))
d2quantity=int(input("enter 2nd dish quantity"))
d3quantity=int(input("enter 3rd dish quantity"))
student_discount=0
happyhour=0
large_order=0
price_before_discounts=cost=(d1price*d1quantity)+(d2price*d2quantity)+(d3price*d3quantity)
# student discount and order time
if has_student_id=="yes" and order_time>=14 and order_time<=17:
               price_before_discounts=price_before_discounts-price_before_discounts*0.2
               large_order=1
# happy hour discount
if  order_time>=14 and order_time<=17 and has_student_id=="no":
               price_before_discounts=price_before_discounts-price_before_discounts*0.2
               large_order=1
               happyhour=1
# student discount 
if has_student_id=="yes" and order_time<=14 or order_time>=17:
               price_before_discounts=cost-cost*0.15
               student_discount=1
# large order discounts
if cost>=150000:
               price_before_discounts=cost-cost*0.05
               large_order=1
             
#service charge
price_before_discounts=service_charge=price_before_discounts+price_before_discounts*0.1
#delivery fee
if cost>100000:
               price_before_discounts=delivery_fee=price_before_discounts+15000
else:
    delivery_fee=0
print('-----------------------')           
print('customer name:',name,'--- student status:',has_student_id,'--- order time:',order_time)
print('dish 1 name:',dish1,'dish 1 cost:',d1price,'dish 1 quantity:',d1quantity)
print('dish 2 name:',dish2,'dish 2 cost:',d2price,'dish 2 quantity:',d2quantity)
print('dish 3 name:',dish3,'dish 3 cost:',d3price,'dish 3 quantity:',d3quantity)
print('subtotal before discounts',cost)
print('-----------------------')   
if has_student_id=='yes':
               print('student discount: True', 'amount',cost*0.15 )
if order_time>=14 and order_time<=17:
    print('happy hour eligibility:True', 'amount', cost*0.2)
if large_order==1:
               print('large order disvount:True', 'amount',cost*0.05)
discounts_total=0
if happyhour==1:
               print("Applied discount: happy hour disvount")
               discounts_total+=cost*0.2
if student_discount==1:
               print("Applied discount: student discount")
               discounts_total+=cost*0.15
if large_order==1:
               print("Applied discount: large order discount")
               discounts_total+=cost*0.05
print('-----------------------')   
print('total discounts:',discounts_total)
print("subttotal after discount:",cost-discounts_total)
print('service cahrge amount:',service_charge)
print('delivery fee:',delivery_fee)
print('total:',price_before_discounts)
print('savings:', price_before_discounts-discounts_total)

               

