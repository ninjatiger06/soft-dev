public boolean isBalanced(ArrayList<String> delimiters)
{
  private int numOpen;
  private int numClosed;

  numOpen = 0;
  numClosed = 0;

  for (String str : delimiters)
  {
    if (str.equals(openDel))
    {
      numOpen++;
    }
    else
    {
      numClosed++;
    }
    if (numClosed > numOpen)
    {
      return false;
    }
  }
  if (numOpen == numClosed)
  {
    return true;
  }
  else
  {
    return false;
  }
}
