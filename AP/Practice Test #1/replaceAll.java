{
  int repIndex = text.indexOf(what);
  str newString = text[0:repIndex];
  SavedText.add(text);

  while (repIndex > 0) {
    newString += sub;
    repIndex = text.indexOf(what);
    newString += text[newString.length() : repIndex];
  }
  return newString;
}
