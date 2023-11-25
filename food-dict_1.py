order = {
    'client': 'john',
    'item': 'salad',
    'quantity': 5,
    'price': 15.00
}

order['total'] = order['price'] * order['quantity']

# Aplicați o reducere de 20% dacă cantitatea este mai mare de 7
if order['quantity'] > 7:
    order['discount'] = 0.2
    order['total'] *= (1 - order['discount'])

print("ORDER FOR :", order['client'])
print("FOOD      :", order['item'])
print("pric x qty:", order['price'], 'x', order['quantity'])
print("total     :", order['total'])

# Întrebați utilizatorul dacă are nevoie de livrare
delivery_answer = input("Do you need delivery? (yes/no): ")

# Verificați dacă totalul este mai mare de 300 și utilizatorul dorește livrarea
if order['total'] > 300 and delivery_answer == 'yes':
    order['delivery'] = 'free'
    print("Delivery   :", order['delivery'])
else:
    order['delivery'] = 'not free'

print("Final Total:", order['total'])

