public int findLastOccurence(String str)
{
  int n = 1;
  while (findNthOccurence(str, n+1) != -1)
  {
    n++
  }
  return findNthOccurence(str, n);
}
