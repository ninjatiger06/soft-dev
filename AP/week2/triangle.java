/*
Description: This program will create a triangle using a certain character up
             to a certain number of lines
Author: Jonas Pfefferman '24
Date: 1/29/20
*/

import java.util.Scanner;

public class triangle {
    public static void main(String[] args) {
        String character;
        Scanner charScan;
        Integer num;
        Scanner numScan;
        Integer counter;

        charScan = new Scanner(System.in);
        System.out.println("Character:");
        character = charScan.next();

        numScan = new Scanner(System.in);
        System.out.println("Number of lines:");
        num = numScan.nextInt();

        counter = 1;
        for (Integer i = 0; i < num; i++) {
            for (Integer x = 0; x < counter; x++) {
                System.out.print(character);
            }
            counter += 1;
            System.out.println();
        }
    }
}