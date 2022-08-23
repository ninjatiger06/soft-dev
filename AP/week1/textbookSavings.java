/*
 Description: This program will take your savings and calculate how many of
                 an item you can get with them
    Author: Jonas Pfefferman '24
    Date: 1/27/21
*/

import java.util.Scanner;

public class textbookSavings {

    public static void main(String[] args) {
        Double bookSavings;
        String purchaseItem;
        Double itemCost;
        //Double numberItems;
        //Integer numberItemsInt;
        Scanner savings;
        Scanner item;
        Scanner cost;

        savings = new Scanner(System.in);
        System.out.println("Enter textbook savings: ");
        bookSavings = savings.nextDouble();

        item = new Scanner(System.in);
        System.out.println("What would you like to purchase instead of a book? ");
        purchaseItem = item.nextLine();

        cost = new Scanner(System.in);
        System.out.println("Enter item cost: ");
        itemCost = cost.nextDouble();

        Double numberItems = bookSavings / itemCost;
        Integer numberItemsInt = (Integer)numberItems;

        System.out.println("You could buy " + numberItemsInt + " " + purchaseItem + "(s) with your textbook savings.");
    }
}