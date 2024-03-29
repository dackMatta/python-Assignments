#Dictionaries

#customer={
 #"name":"mac thee great",
  #  "age":34,
 #   "isMarried":True,
#}
#customer['birthdate']='1 jan 1999'
#print('Customers name:', customer["name"],'age:', customer["age"],customer["isMarried"], customer['birthdate']  )

phone=input('enter phone number: ')
dig_map={
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
}
output=''
for numb in phone:
    output += dig_map.get(numb, '!') + ' '
print(output)