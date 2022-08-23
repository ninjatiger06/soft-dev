public WordPairList (String[] words) {
  allPairs = new ArrayList<WordPair>();

  for (int i = 0; i < words.length-1; i++) {
    for (int j = 0; j < words.length(); j++) {
      allPairs.add(new WordPair(words[i], words[j])));
    }
  }
}
