public void replaceNthOccurance(String str, int n, String repl)
{
  private String clear = findNthOccurence(str, n);

  if (clear != -1)
  {
    currentPhrase = currentPhrase.substring(0, clear) + repl + currentPhrase.substring(clear + str.length);
  }
}
