public static Position findPosition(int num, int[] [] intintArr)
{
  for (int row = 0; row < intArr.length(); row++)
  {
    for (int column = 0; column < intArr[row].length(); column++)
    {
      if (num == intArr[row][column])
      {
        return new Position(row, column);
      }
    }
  }
  return null;
}
