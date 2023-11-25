order = {
    'client': 'john',
    'item': 'salad',
    'quantity': 5,
    'price': 15.00
}

order['total'] = order['price'] * order['quantity']

# Aplică o reducere de 20% dacă cantitatea este mai mare de 7
if order['quantity'] > 7:
    order['discount'] = 0.2
    order['total'] *= (1 - order['discount'])

# Întreabă utilizatorul dacă are nevoie de livrare
delivery_input = input("Do you need delivery? (yes/no): ")

if delivery_input == 'yes':
    order['delivery'] = 50.00
    order['total'] += order['delivery']

print("ORDER FOR :", order['client'])
print("FOOD      :", order['item'])
print("pric x qty:", order['price'], 'x', order['quantity'])
print("total     :", order['total'])

if 'discount' in order:
    print("discount  :", order['discount'] * 100, '%')

if 'delivery' in order:
    print("delivery  :", order['delivery'])

