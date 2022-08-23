public static Position[] [] getSuccessorArray(int[] [] intArr)
{
  int newArr [intArr.length()] = new int[intArr.length()];
  for (int row = 0; row < intArr.length(); row++)
  {
    for (int column = 0; column < intArr[0].length(); row++)
    {
      pos = findPosition(intArr[row][column], intArr)
      newArr.add(pos);
    }
  }
  return newArr
}
