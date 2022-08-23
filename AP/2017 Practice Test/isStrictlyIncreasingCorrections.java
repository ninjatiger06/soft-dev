public boolean isStrictlyIncreasing()
{
  for (int i = 0; i < digitList.size()-1; i++)
  {
    if (digitList.get(i).intValue() >= digitList.get(i+1).intValue())
    {
      return false;
    }
  }
  return true;
}
