public double runSimulations (int num){
  int countSuccess = 0;

  for (int count = 0; count < num; count++) {
    if (simulate()) {
      countSuccess++;
    }
  }
  return (double) countSuccess / num;
}
