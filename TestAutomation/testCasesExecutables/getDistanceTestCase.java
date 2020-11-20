public class getDistanceTestCase {
    public static void main(String[] args) {
        try {
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
        double distance = pointOne.getDistance(pointTwo);

        System.out.println("Test:");
        System.out.printf("Caculate distance bettween (%f,%f) and (%f,%f)\n", pointOneX, pointOneY, pointTwoX, pointTwoY);

        System.out.println("Result: " + distance);

        // Test passed
        if (distance == testOracle) {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Pass");
        }
        // Test failed
        else {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Fail");
        }
        } catch (Exception e) {
            System.out.println("ERROR");
        }
    }
}