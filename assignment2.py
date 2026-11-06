small=3.50
medium=4.50
large=5.50
total=0
print('=== Coffee Shop Order System ===')
print('Enter drink sizes: small, medium, or large')
print('Type done when finished ordering')
enter=input('Enter drink size:')
while enter!='done':
    if enter=='small':
        c=small
    elif enter=='medium':
        c=medium
    elif enter=='large':
        c=large
    else:
        print('please write small , medium, large or done')
        enter=input('Enter drink size:')
        continue
    total+=c
    print(f'Price:$ {c:.2f}')
    print(f'Current total:$ {total:.2f}')
    enter=input('Enter drink size:')
print('=== Order Summary ===')
print(f'Subtotal:$ {total:.2f}')
if total>=20.00:
    total-=3
    print('Loyalty Discount: -$3.00')
print(f'Final Total:$ {total:.2f}')
print('Thank you for your order!')
