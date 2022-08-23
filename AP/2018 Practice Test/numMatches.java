public int numMatches() {

  int count = 0;

  for (wordPair pair: allPairs){
    if (pair.getFirst().equals(pair.getSecond))
    {
      count ++;
    }
  }
  return count;
}
