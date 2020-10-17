public class testCase4 {
    public static void main(String[] args) {

        // Get values from input
        double pointOneX = Double.parseDouble(args[0]);
        double pointOneY = Double.parseDouble(args[1]);
        double pointTwoX = Double.parseDouble(args[2]);
        double pointTwoY = Double.parseDouble(args[3]);

        // Instantiate two points
        PhaseSpaceCoordinate pointOne = new PhaseSpaceCoordinate(pointOneX, pointOneY);
        PhaseSpaceCoordinate pointTwo = new PhaseSpaceCoordinate(pointTwoX, pointTwoY);

        // Grab the oracle from the input
        double testOracle = Double.parseDouble(args[4]);

        // Get the distance bettween two points
        double distance = pointOne.compareTo(pointTwo);

        System.out.println("Test Four:");
        System.out.printf("Compare Points (%f,%f) and (%f,%f)\n", pointOneX, pointOneY, pointTwoX, pointTwoY);

        System.out.println("Result: " + distance);

        // Test passed
        if (distance == testOracle) {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Test four passed!");
        }
        // Test failed
        else if (distance != testOracle) {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Test four failed...");
        }
        // Test ERROR
        else {
            System.out.println("Test four ERROR");
        }

    }
}