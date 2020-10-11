
public class testCase1 {
    public static void main(String[] args) {

        // Instantiate the Binomial Distribution Utility class
        BinomialDistributionUtil BinomialDistributionUtil = new BinomialDistributionUtil();

        // Test 1: Normal numerical value in range
        int testOne = Integer.parseInt(args[0]);
        
        // Run the actual method we are testing
        double value = BinomialDistributionUtil.lnFactorial(testOne);

        // Print test number
        System.out.println("Test one:");
        System.out.println("ln(" + testOne + "!): " + value);

        // Print out test result
        double testOneOracle = Double.parseDouble(args[1]);

        // Test passed
        if (value == testOneOracle) {
            System.out.println("Oracle: " + testOneOracle);
            System.out.println("Test one passed!");
        }
        // Test failed
        else if (value != testOneOracle) {
            System.out.println("Oracle: " + testOneOracle);
            System.out.println("Test one failed...");
        }
        // Test ERROR
        else {
            System.out.println("Test one ERROR");
        }
    }
}