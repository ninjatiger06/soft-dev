public static Position[] [] getSuccessorArray(int[] [] intArr)
{
  Position[] [] newArr = new Position[intArr.length()][intArr[0].length];
  for (int row = 0; row < intArr.length(); row++)
  {
    for (int column = 0; column < intArr[0].length(); colmun++)
    {
      newArr[row][column] = findPosition(intArr[row][col]+1, intArr);
    }
  }
  return newArr
}
