def main():
    print("Yay")

if __name__ == "__main__":
    main()

name = "Zach"

#print("hello {}".format(name))



x = 10
#print(x)

#def LessThanGreaterThan(num):
    #print(num)

  #  num = int(input("enter a number"))
  #  print(num)
  #  if num > 10:
   #     print("{} is greater than 10".format(num))

    #if num < 10:
       # print("{} is less than 10".format(num))
    #if num == 10:
     #   print("the number is 10")
#LessThanGreaterThan(10)












#4. Write a program that takes a number as a user input and tells
#the user if it is even or odd.
#5. Create a list and write a program that prints each individual
#element to the console.

favoriteFoods = ["donuts", "ice cream", "sushi", "pizza"]

#print(favoriteFoods[2])
for food in favoriteFoods:
    print(food)



#6. Write a program that uses a loop fill an empty list with 10
#numbers and prints the list to the console. The numbers can
#be random or simply put in the numbers 0-9 or 1-10 in
#ascending order.

myemptylist = []
for number in range(11):
    print(number)
myemptylist.append(number)


#7. Write a program that takes a number as user input and tells
#you how many numbers in a list are less than the number that
#the user gave.
#8. Write a program that keeps asking the user to enter a word.
#For each word that the user enters, the program prints out
#each letter in the word on a new line. When the user enters
#“s 