# Calculator Project

A simple Python calculator project to demonstrate pytest coverage reporting with GitHub Actions.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Power calculation
- Average calculation
- Factorial calculation
- Comprehensive pytest test suite
- GitHub Actions workflow for automated testing
- Pytest coverage report generation and PR comments

## Project Structure

```
calculator_project/
├── .github/
│   └── workflows/
│       └── pytest-coverage.yml
├── calculator/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── requirements.txt
└── README.md
```

## How to Run Tests Locally

1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the tests: `pytest`
4. Generate coverage report: `pytest --cov=calculator --cov-report=html tests/`
5. Open `htmlcov/index.html` in your browser to view the HTML coverage report

## CI/CD Integration

This project includes a GitHub Actions workflow that:

1. Runs on push to main and on pull requests
2. Executes all tests with pytest
3. Generates coverage reports in multiple formats
4. Comments on pull requests with coverage statistics
5. Archives HTML coverage report as a workflow artifact

## Coverage Badge

<!-- Pytest Coverage Comment:Begin -->
<!-- Coverage badge will be automatically updated here by the GitHub Action -->
<!-- Pytest Coverage Comment:End -->

## License

MIT