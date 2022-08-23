import javax.swing.JOptionPane;         // use import to access built-in Java classes (i.e. a 'package')

public class RandomNum
{
     public static void main(String[] args)
     {
          int random = (int) (Math.random() * 10);
          int num = 1 + random;         // in case random comes out to zero
          JOptionPane.showMessageDialog(null, "The random number is " + num);

          double random2 = Math.random();
          double num2 = 1 + random2; 
          JOptionPane.showMessageDialog(null, "The random number is " + num2);
     }
}
