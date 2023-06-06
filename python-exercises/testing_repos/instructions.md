# Python Testing Exercises

Practice of testing with Pytest in a Python environment

## Organisation

### Duration

Two exercises:

- Exercise #1: 1h
- Exercise #2: 1h

Note that times are approximate and you can decide how much time you spend on each exercise

Make sure to take breaks!

### Team

Same pairs of the previous day

## Brief

### Exercise #1

Under the `testing_repos` folder, you will find two applications: `api-testing` and `essentials`. Each application includes some tests already, but when running `pipenv run coverage`, not all lines are covered.

Your task is to get each test suite to 100%! It's very close!

Each folder in this repo has its own installation requirements. Follow these simple steps to get the tests running and make sure to switch envs between each one:

- `cd <folder>`
- `pipenv shell` to start the virtual environment
- `pipenv install` to install dependencies
- `pipenv run test` to run the tests,
- `pipenv run coverage` to run the tests with coverage output
- `exit` to leave the virtual environment

### Exercise #2

Using any activity/project you have worked on this week, write tests for them. Make sure you practice:

- Regular tests (assert...)
- Parametrize
- Throwing errors
- Mocking & MonkeyPatch
- Coverage

---

[Back](./README.md)

---