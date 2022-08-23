public static int dayOfWeek(int month, int day, int year)
{
  int day1 = firstDayOfYear(int month, int day, int year);
  int dayOfWeek = day1;

  for (int day# = day1; day# <= dayOfYear(int month, int day, int year); day#++)
  {
    if (dayOfWeek == 6)
    {
      dayOfWeek = 0
    }
    else
    {
      dayOfWeek++;
    }
  }
  return dayOfWeek;
}
