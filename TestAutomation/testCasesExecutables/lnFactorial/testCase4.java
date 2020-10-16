
public class testCase4 {
    public static void main(String[] args) {

        // Instantiate the Binomial Distribution Utility class
        BinomialDistributionUtil BinomialDistributionUtil = new BinomialDistributionUtil();

        // Test 4: Normal numerical value in range
        int testFour = Integer.parseInt(args[0]);
        
        // Run the actual method we are testing
        double value = BinomialDistributionUtil.lnFactorial(testFour);

        // Print test number
        System.out.println("Test four:");
        System.out.println("ln(" + testFour + "!): " + value);

        // Print out test result
        double testOracle = Double.parseDouble(args[1]);

        // Test passed
        if (value == testOracle) {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Test one passed!");
        }
        // Test failed
        else if (value != testOracle) {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Test one failed...");
        }
        // Test ERROR
        else {
            System.out.println("Test one ERROR");
        }
    }
}