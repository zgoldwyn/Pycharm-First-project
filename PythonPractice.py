def main():
    print(" ")

if __name__ == "__main__":
    main()

name = "Zach"

#print("hello {}".format(name))


#global x
#x = 50
#def change():
 #   global x
  #  x = 50
#print(x)

#def LessThanGreaterThan(num):



 #   num = int(input("enter a number "))
  #  if num > x:
      #  print("{} is greater than 50".format(num))

    #if num < x:
     #   print("{} is less than 50".format(num))
    #if num == x:
     #   print("the number is 50")
    #if num == x:
      #  print(" ")
    #else:
   #         print("yay {} is your number".format(num))
#LessThanGreaterThan(x)
pi = 3.1415
print("Volume and Surface Area of Rectangular Prism")

l = int(input("Length = "))
w = int(input("Width = "))
h = int(input("Height = "))
vorp = l * w * h
sorp = 2*l*w + 2*l*h + 2*w*h
print("volume = {}un‎³".format(vorp))
print("Surface Area = {}un²".format(sorp))

print(" ")

print("Volume and Surface Area of Cylinder")

r = int(input("Radius = "))
h = int(input("Height = "))
voc = 3.1415 * r * r * h
soc = (2 * pi * r * h)+(2 * pi * r * r)
print("Volume = {}un‎³".format(voc))
print("Surface Area = {}un²".format(soc))

print(" ")

print("Volume and Surface Area of Sphere")

r = int(input("Radius = "))
vos = 4.1887 * r * r * r
sos = 4 * pi * r * r
print("Volume = {}un‎³".format(vos))
print("Surface Area = {}un²".format(sos))

print(" ")

print("Volume of Cone")

r = int(input("Radius = "))
h = int(input("Height = "))
VolumeOfCone = pi * r * r * h / 3
print("Volume = {}un‎³".format(VolumeOfCone))



#4. Write a program that takes a number as a user input and tells
#the user if it is even or odd.
#5. Create a list and write a program that prints each individual
#element to the console.

#favoriteFoods = ["donuts", "ice cream", "sushi", "pizza"]

#print(favoriteFoods[2])
#for food in favoriteFoods:
 #   print(food)



#6. Write a program that uses a loop fill an empty list with 10
#numbers and prints the list to the console. The numbers can
#be random or simply put in the numbers 0-9 or 1-10 in
#ascending order.

#myemptylist = []
#for number in range(11):
  #  print(number)
#myemptylist.append(number)


#7. Write a program that takes a number as user input and tells
#you how many numbers in a list are less than the number that
#the user gave.
#8. Write a program that keeps asking the user to enter a word.
#For each word that the user enters, the program prints out
#each letter in the word on a new line. When the user enters
#“s 