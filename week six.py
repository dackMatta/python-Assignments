#Nested Loop
#for x in range(4):
 #   for y in range(3):
  #      print(f'({x}, {y})')

#numbers=[1,1,1,1,6,]
#for x_count in numbers:
 #   output=''
  #  for count in range(x_count):
   #     output+='x'
    #print(output)

numbers=[1,2,3,4,5,7,8,7,4,5]
unique=[]
for number in numbers:
    if number not in unique:
     unique.append(number)
print(unique)