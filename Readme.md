
# Validation and Verification Document

## 1. Introduction
This document outlines the Validation and Verification (V&V) process for the automated test bench implemented via a Bash script. The test bench is designed to validate a specific algorithm according to provided business rules.

## 2. Environment Setup
**Script:** `setup_environment.sh`
- **Objective:** Prepare the test environment by installing necessary dependencies, including Python, and configuring settings specific to the OS.
- **Execution:** Automatically initiated by the main script `run_test.sh`. It detects the OS and installs Python if not already present.

## 3. Test Execution
**Script:** `run_test.sh`
- **Location:** Located in the `script` folder.
- **Operation:**
  1. **Setup:** Initializes the environment by running `setup_environment.sh`.
  2. **Tests:** Iterates through all test directories under `../tests/` and executes the script `run_test.sh` in each subdirectory.
  3. **Error Logging:** Redirects errors to `../results/error.log`.
  4. **Cleanup:** Runs `cleanup_environment.sh` to reset the environment post-testing.

## 4. Result Management
- **Results Folder:** `../results/`
  - **Output Files:** The results of each test are saved in the format `output_<test_directory_name>.csv`.
  - **Test Summary:** A `results_summary.txt` file is updated for each test indicating whether the test passed or failed.
  - **Differences:** For failed tests, differences are recorded in `diff_<test_directory_name>.txt`.

## 5. Evaluation Criteria
- **Test Validity:** Tests are deemed valid if the complete process is executed without errors and the output files match expected results.
- **Automation:** The testing process is fully automated, requiring no manual intervention once the initial script `run_test.sh` is started.

## 6. Conclusion
This test bench provides an automated and reliable evaluation of the algorithm as per the provided specifications. It ensures comprehensive test coverage through automated result verification and detailed error logging.

### Usage
To run the test bench:
1. Navigate to the `script` folder.
2. Execute the script with the command: `./run_test.sh`.

Ensure all scripts (`setup_environment.sh`, `run_test.sh`, `cleanup_environment.sh`) are executable. You can make them executable using the command: `chmod +x <script_name>.sh`.
