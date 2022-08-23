public static int numberOfLeapYears(int year1, int year2)
{
  int count = 0;
  for (int y = year1; y <= year2; y++)
  {
    if (isLeapYear(y))
    {
      count ++;
    }
  }
  return count;
}
