/*
Description: This program will computer the cost of a multi-day trip for one or
             more people.
Author: Jonas Pfefferman '24
Date: 1/29/21
*/

import java.util.Scanner;

public class tripCost {
    public static void main(String[] args) {
        Double personTravel;
        Double personFood;
        Integer travelDays;
        Integer numberPeople;
        Double personTotalBill;
        Double totalBill;
        Scanner personTravelCost;
        Scanner personFoodCost;
        Scanner days;
        Scanner numberOfPeople;

        personTravelCost = new Scanner(System.in);
        System.out.println("What is the travel cost per person?");
        personTravel = personTravelCost.nextDouble();

        personFoodCost = new Scanner(System.in);
        System.out.println("What is the food/lodging cost per person per day?");
        personFood = personFoodCost.nextDouble();

        days = new Scanner(System.in);
        System.out.println("How many days will you be traveling?");
        travelDays = days.nextInt();

        numberOfPeople = new Scanner(System.in);
        System.out.println("How many people are going?");
        numberPeople = numberOfPeople.nextInt();

        personTotalBill = (personFood * travelDays) + personTravel;

        totalBill = personTotalBill * numberPeople;

        System.out.println("Cost per person: $" + personTotalBill);
        System.out.println("Total cost: $" + totalBill);
    }
}