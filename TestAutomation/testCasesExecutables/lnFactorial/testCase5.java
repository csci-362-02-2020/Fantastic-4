
public class testCase5 {
    public static void main(String[] args) {

        // Instantiate the Binomial Distribution Utility class
        BinomialDistributionUtil BinomialDistributionUtil = new BinomialDistributionUtil();

        // Test 5: Normal numerical value in range
        int testFive = Integer.parseInt(args[0]);
        
        // Run the actual method we are testing
        double value = BinomialDistributionUtil.lnFactorial(testFive);

        // Print test number
        System.out.println("Test five:");
        System.out.println("ln(" + testFive + "!): " + value);

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