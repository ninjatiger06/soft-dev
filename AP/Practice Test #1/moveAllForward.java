{
  for (int i = 0; i < hwy.length(); i++) {
    for (int j = 0; j < hwy[i].length(); j++) {
      if (j + 1 > hwy[i].length()) {
        hwy[i][j] = 0;
        hwy[i][0] = 1;
      }
      hwy[i][j] = 0;
      hwy[i][j+1] = 1;
    }
  }
}
