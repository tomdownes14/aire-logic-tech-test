# Aire Logic Tech Test

## Execution

### Requirements

- Windows OS x64
- Python 3.6+
- Chrome 85
- Firefox 79

### Run Test Suites

__chrome__ - `python3 -m unittest`

__firefox__ - `BROWSER=firefox python3 -m unittest`

## Approach

A simple test plan was created to outline the testing process - [docs/TEST-PLAN.md](docs/TEST-PLAN.md)

### Gather Requirements

The requirements of the product are "a clone of the cookie clicker game". To understand the product and create test cases an investigation was done against [this version of the game](https://orteil.dashnet.org/cookieclicker/). This version was then compared against the application under test to determine which features are being replicated. Some functionality has been infered from usage of AUT (price p/factory, price p/cookie)

### Create Test Cases

Test cases were defined before any scripting began. This ensures that test cases aren't influenced by current functionality.

### Script Test Cases

Test cases were scripted using Selenium & Python. The page object model pattern was implemented. 

N.B some test cases are more suitable for component testing such as `test_can_buy_factory_with_money`. 

This test (and others) will always fail due to other broken funcionality (unable to correctly sell cookies). Testing this with an automated e2e tool is not ideal. Bugs for these tests have been captured through manual testing.

### Record Issues

Issues have been recorded in a Markdown document.

## Going Forward

Given more time and resources I would like to have done the following:

- Re-use browser sessions where appropriate
- Control test data
- Generate test reports
- Unit tests for individual UI components
- Unit/Integration tests for the JSON RPC endpoint
- Non-functional testing for Web & JSON RPC endpoint
- Accessiblity testing
- Security testing