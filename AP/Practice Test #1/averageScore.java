{
  if (scores.length() >= 6) {
    Array<int>[2] maxAndMin = scores.findMaxAndMin(int[] scores);
    if (scores.countOccurrences(maxAndMin[0]) == 1) {
      scores.remove(maxAndMin[0]);
    }
    else if (scores.countOccurrences(maxAndMin[1]) == 1) {
      scores.remove(maxAndMin[1]);
    }
  }
  int total = 0;
  for (score : scores) {
    total += score;
  }
  double average = total / scores.length();
  return average;
}
