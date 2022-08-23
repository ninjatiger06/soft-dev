public class loopTest {

  public static void main(String[] args) {
    System.out.println("For loop 2,101,2");
    for (Integer i = 2; i < 101; i+=2) {
      System.out.println(i);
    }
    System.out.println("For loop 1,100");
    for (Integer i = 2; i < 101; i++) {
      System.out.println(i);
    }
    System.out.println("For loop 100,0,-1");
    for (Integer i = 100; i < 0; i--) {
      System.out.println(i);
    }
  }
}
