{
  if (lane + dir > hwy.length()) || (lane + dir < 0) {
    return false;
  }
  else if (hwy[lane + dir][x] == 1) {
    return false;
  }
  else {
    return true;
  }
}
