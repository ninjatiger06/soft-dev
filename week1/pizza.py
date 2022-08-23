#This is a calculator for friends to see how much money they will spend on pizza, how many slices
#each person gets, etc.
#author: Jonas Pfefferman '24
#Date: 8/31/20

import math

def main ():

    friends = int(input("Number of friends: "))
    pizzas = int(input("Number of pizzas: "))
    slices = 8
    tip = float(input("Tip (%): "))
    trueTip = tip / 100
    pizzaDiameter = int(input("Diameter of a pizza (inches): "))
    pizzaCost = 12
    deliveryFee = 10

    totalCost = pizzas * pizzaCost
    tipAmount = totalCost * trueTip
    totalBill = totalCost + tipAmount + deliveryFee

    costPerson = totalBill / friends
    totalSlices = pizzas * 8
    slicesPerson = totalSlices / friends

    pi = 3.14159265358979323
    pizzaRadius = pizzaDiameter / 2
    #pizzaArea = math.pi * (pizzaRadius * pizzaRadius)
    pizzaArea = pi * (pizzaRadius * pizzaRadius)

    #print("Total: $", totalCost)
    print("Total: $" + str(totalBill))
    print("Cost per Person: " + str(costPerson))
    print("Slices per Person: " + str(slicesPerson))
    print("Area of one pizza: " + str(pizzaArea), "Square Inches")

main()
