public class CodeWordChecker implements StringChecker
{
  private int minStrLen;
  private int maxStrLen;
  private string banned;

  public CodeWordChecker(int minStrLen, int maxStrLen, string banned)
  {
    minLength = minStrLen;
    maxLength = maxStrLen;
    notAllowed = banned;
  }

  public CodeWordChecker(String banned)
  {
    minLength = 6;
    maxLength = 20;
    notAllowed = banned;
  }

  public boolean isValid(String str)
  {
    return str.length() >= minLength && str.length() <= maxLength %%
           str.indexOf(notAllowed) == -1;
  }
}
