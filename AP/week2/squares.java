/*
    Description: This program will calculate all the squares up to a certain number
    Author: Jonas Pfefferman '24
    Date: 2/3/21
*/

import java.util.Scanner;

public class squares {
    public static void main(String[] args) {
        Scanner numberScan;
        Integer endNumber;
        Integer number;
        Integer square;

        numberScan = new Scanner(System.in);
        System.out.println("End Number:");
        endNumber = numberScan.nextInt();

        number = 1;
        for (Integer i = 1; i < endNumber + 1; i++) {
            square = number * number;
            System.out.println(number + " x " + number + " = " + square);
            number += 1;
        }
    }
}