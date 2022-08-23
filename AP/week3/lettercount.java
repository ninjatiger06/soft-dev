/*
    Description: This program counts the number of a certain letter in an
                 inputted string.
    Author: Jonas Pfefferman '24
    Date: 2/8/21
*/

import java.util.Scanner;

public class lettercount {
    public static void main(String [] args) {
        Scanner scan;
        String phrase;
        String letter;
        Integer letterCount;
        String charString;
        Character c;

        scan = new Scanner (System.in);
        System.out.print("phrase: ");
        phrase = scan.next();
        System.out.print("letter: ");
        letter = scan.next();

        letterCount = 0;
        for (Integer i = 0; i < phrase.length(); i++) {
            c = phrase.charAt(i);
            charString = String.valueOf(c);
            if (charString.equals(letter)) {
                letterCount ++;
            }
        }

        if (letterCount == 1) {
            System.out.println(String.format("There is 1 %s in %s.", letter,
            phrase));
        }

        else {
            System.out.println(String.format("There are %d %s's in %s.",
            letterCount, letter, phrase));
        }
    }
}
