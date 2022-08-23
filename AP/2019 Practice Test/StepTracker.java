public class StepTracker
{
  private int minSteps;
  private int totalSteps;
  private int numDays;
  private int numActiveDays;

  public StepTracker(int minnum)
  {
    minSteps = minnum;
    totalSteps = 0;
    numDays = 0;
    numActiveDays = 0;
  }

  public void addDailySteps(int numSteps)
  {
    totalSteps += numSteps;
    numDays ++
    if (numSteps >= steps)
    {
      numActiveDays++;
    }
  }

  public int activeDays
  {
    return activeDays;
  }

  public double averageSteps()
  {
    if (numDays == 0)
    {
      return 0.0;
    }
    else
    {
      return (double) totalSteps / numDays;
    }
  }
}
