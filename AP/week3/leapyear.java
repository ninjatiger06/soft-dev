/*
    Description: This program prompts the user for a year and then prints
                    whether or not that year is a leap year.
        Author: Jonas Pfefferman '24
        Date: 2/3/21
*/

import java.util.Scanner;

public class leapyear {
    public static void main(String[] args) {
        Scanner yearScan;
        Integer year;
        String isLeapyear;
        String notLeapyear;

        yearScan = new Scanner (System.in);
        System.out.print("Enter a year: ");
        year = yearScan.nextInt();

        if (year % 100 == 0) {
            if (year % 400 == 0) {
                isLeapyear = String.format("%d is a leap year.", year);
                System.out.println(isLeapyear);
            } else {
                notLeapyear = String.format("%d is NOT a leap year.", year);
                System.out.println(notLeapyear);
            }
        } else if (year % 4 == 0) {
            isLeapyear = String.format("%d is a leap year.", year);
            System.out.println(isLeapyear);
        } else {
            notLeapyear = String.format("%d is NOT a leap year.", year);
            System.out.println(notLeapyear);
        }
    }
}