weekday=8.00
weekend=6.00
holiday=5.00
total=0
print('===  Parking Garage Calculator ===')
print("Enter day type: weekday, weekend, or holiday")
print('Type done when finished entering hours')
enter=input('Enter day type for 1 hour: ')
while enter!='done':
    if enter=='weekday':
        c=weekday
    elif enter=='weekend':
        c=weekend
    elif enter=='holiday':
        c=holiday
    else:
        print('please write  weekday, weekend, holiday or done')
        enter=input('Enter day type for 1 hour: ')
        continue
    total+=c
    print(f'Price:$ {c:.2f}')
    print(f'Current total:$ {total:.2f}')
    enter=input('Enter day type for 1 hour: ')
print('=== Parking Summary ===')
print(f'Subtotal:$ {total:.2f}')
if total>=50.00:
    total-=7
    print('Frequent Parker Discount: -$7.00')
print(f'Final Total:$ {total:.2f}')
print('Thank you for parking with us!')
