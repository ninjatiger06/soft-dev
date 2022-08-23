{
  if (savedText.length() == 0) {
    return null;
  }
  else {
    string ogText = savedText[0];
    int repIndex = text.indexOf(sub);

    while (repIndex > 0) {
      text[repIndex] = ogText;
      repIndex = text.indexOf(sub);
    }
    return text;
  }
}
