public LightBoard(int numRows, int numCols)
{
  lights = new boolean[numRows][numCols];
  for (int r = 0; r < numRows; r++)
  {
    for (int c = 0; c < numCols; c++)
    {
      double rnd = Math.random();
      lights[r][c] = rnd < 0.4;
    }
  }
}
