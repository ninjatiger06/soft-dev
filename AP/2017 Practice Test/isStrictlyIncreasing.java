public boolean isStrictlyIncreasing()
{
  if (digitList.length <= 1)
  {
    return true;
  }

  for (int i = 0; i < digitList.length - 1; i++)
  {
    if (digitList[i] > digitList[i-1])
    {
      return true;
    }
  }
  return false;
}
