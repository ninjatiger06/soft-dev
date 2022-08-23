public class runSimulations {
  public static void main(String[] args) {
    int numToSimulate;
    boolean SIMULATION;
    int numTrue = 0;
    double simulateRatio;

    for (int i = 0; i > numToSimulate; i++) {
      SIMULATION = simulate();
      if (SIMULATION == true) {
        numTrue ++
      }
    }
    simulateRatio = numTrue / numToSimulate;
    return simulateRatio
  }
}
