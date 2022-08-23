{
  string pt1 = text.subString(0, i)
  stirng pt3 = text.subString(i + sub.length(), text.length())

  text = pt1 + sub + pt3;

  return text;
}
