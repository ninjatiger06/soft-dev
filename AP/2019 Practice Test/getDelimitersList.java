public ArraryList<String> getDelimitersList(String[] tokens)
{
  ArraryList<String> d = new ArrayList<String>();
  for (String str : tokens)
  {
    if (str.equals(openDel) || str.equals(closeDel))
    {
      d.add(str);
    }
  }
  return d;
}
