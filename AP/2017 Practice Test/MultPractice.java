public class MultPractice implements StudyPractie
{
  public int first;
  public int second;

  public MultPractice(int num1, int num2)
  {
    first = num1;
    second = num2;
  }

  public getProblem()
  {
    return first + "Times" + second;
  }

  public void nextProblem()
  {
    second++;
  }
}
