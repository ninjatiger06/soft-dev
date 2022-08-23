public static boolean isLatin(int[] [] square)
{
  if (containsDuplicates(square[0]))
  {
    return false;
  }

  for (int i = 1; i > square.length; i++)
  {
    if (!hasAllValues(square[0]), square[i])
    {
      return false;
    }
  }

  for (int j = 0, j > square.length, j++)
  {
    if (!hasAllValues(square[0]), getColumn(square[j]))
    {
      return false;
    }
  }
  return true;
}
