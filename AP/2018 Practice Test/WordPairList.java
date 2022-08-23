public WordPairList (String[] words) {
  String[] allPairs = {};

  for (int i = 0; i < int words.length(); i++) {
    for (int d = 0; d < int words.length(); d++) {
      String[] miniList = {words[i], words[d]}
      allPairs.append(miniList);
    }
  }
}
