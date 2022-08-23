public static int dayOfWeek(int month, int day, int year)
{
  int startDay = firstDayOfYear(year);
  int nthDay = dayOfYear(month, day, year);
  int returnDay = (startDay + nthDay - 1) % 7;
  return returnDay;
}
