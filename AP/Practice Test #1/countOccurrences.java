{
  int counter = 0;
  for (score : scores) {
    if (scores[score] == target) {
      counter++;
    }
  }
  return counter;
}
