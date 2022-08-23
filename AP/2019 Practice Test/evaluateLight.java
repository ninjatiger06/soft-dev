public boolean evaluateLight(int row, int col)
{
  int numOn = 0;

  for (int r = 0; r < numRows; r++)
  {
    if (lights[r][col])
    {
      numOn++;
    }
  }

  if (lights[row][col] && numOn % 2 == 0)
  {
    return false;
  }
  if (!lights[row][col] && numOn % 3 == 0)
  {
    return true;
  }
  return lights[row][col];
}
