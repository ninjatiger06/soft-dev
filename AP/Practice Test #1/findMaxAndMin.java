{
  int min = 100;
  int max = 0;

  for (score : scores) {
    if (score < min) {
      min = score;
    }
    else if (score > max) {
      max = score;
    }
  }

  Array<int>[2] maxAndMin = new Array<int>[2];
  maxAndMin.add(max);
  maxAndMin.add(min);
  return maxAndMin;
}
