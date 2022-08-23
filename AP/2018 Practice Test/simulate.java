public boolean simulate {
  public static void main(String[] args) {
    int position = 0;

    for (int I; count < maxHops; count++) {
      if (position >= goalDistance) {
        return true;
      }
      else if (position < 0) {
        return false;
      }
    }
    return false;
  }
}
