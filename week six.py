#Nested Loop
#for x in range(4):
 #   for y in range(3):
  #      print(f'({x}, {y})')

numbers=[1,1,1,1,6,]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output+='x'
    print(output)