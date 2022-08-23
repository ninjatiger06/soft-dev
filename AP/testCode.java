public class testCode
{
  public static void main(String[] args)
  {
    int counter = 0;
    for (int i = 0; i < 15; i++)
    {
      double r = (double) Math.random();
      boolean chance = r < 0.25;
      System.out.println(counter + ": " + chance);
      counter++;
    }
  }
}
