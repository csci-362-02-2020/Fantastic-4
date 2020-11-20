
public class formatLatLngValueTestCase {
    public static void main(String[] args) {
        try {
        // Instantiate the Binomial Distribution Utility class
        LatLong LatLongClass = new LatLong();

        // Test 1: Normal numerical value in range
        double input = Double.parseDouble(args[0]);

        double fractionalDigits = Double.parseDouble(args[1]);

        String testOracle = args[2];
        
        // Run the actual method we are testing
        String result = LatLong.formatLatLngValue(input, fractionalDigits);

        // Print test number
        System.out.println("Test:");
        System.out.println("Format " + input);

        System.out.println("Result: " + result);

        // Test passed
        if (result.equals(testOracle)) {
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