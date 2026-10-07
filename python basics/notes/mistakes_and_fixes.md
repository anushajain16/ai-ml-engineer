# Mistakes and Fixes

This file records common Python mistakes and how they were solved during the 5-day learning journey.

## Day 01 - Python Core

- Mistake: forgetting to convert user input to `int` before doing arithmetic.
  - Fix: use `int(input())` or `float(input())` depending on the requirement.
- Mistake: writing a `while` loop that never ends because the condition never changes.
  - Fix: update the loop variable inside the loop so it moves toward the stopping condition.
- Mistake: using `=` instead of `==` in comparisons.
  - Fix: use `==` to compare values and `=` only for assignment.
- Mistake: creating variable names that are confusing or reused incorrectly.
  - Fix: use clear names like `total_cost`, `num_rooms`, and `discount`.

## Day 02 - OOP

- Mistake: confusing object attributes with local variables.
  - Fix: assign values through `self.attribute_name` inside the class.
- Mistake: calling `self.send()` inside a child method and creating infinite recursion.
  - Fix: use `super().send()` when calling the parent method intentionally.
- Mistake: assuming Python will follow the visual class order instead of the MRO.
  - Fix: check `ClassName.__mro__` to understand method resolution order.
- Mistake: forgetting to call the parent constructor when subclassing.
  - Fix: use `super().__init__(...)` when needed.

## Day 03 - Modules

- Mistake: importing the wrong module path and getting `ModuleNotFoundError`.
  - Fix: ensure the package directory is structured correctly and use the right import path.
- Mistake: writing imports that do not match the file location.
  - Fix: use `from package.module import function` or `import package.module` consistently.
- Mistake: forgetting to create `__init__.py` when using a package structure.
  - Fix: add the package marker file for clear Python package recognition.
- Mistake: mixing file names with function names and creating confusion.
  - Fix: keep module names and function names simple and meaningful.

## Day 04 - File I/O

- Mistake: trying to open a file that does not exist.
  - Fix: use `try` and `except FileNotFoundError` to handle missing files gracefully.
- Mistake: forgetting to close files after reading or writing.
  - Fix: use `with open(...) as file:` so Python closes the file automatically.
- Mistake: using the wrong mode like writing to a file that should be read only.
  - Fix: use `"r"` for reading, `"w"` for writing, and `"a"` for appending.
- Mistake: not checking whether the file path is valid.
  - Fix: use correct relative or absolute paths and verify the working directory.

## Day 05 - Pytest

- Mistake: writing tests with incorrect import paths after moving files into different folders.
  - Fix: update imports to the new package path and keep the package structure consistent.
- Mistake: assuming a test passes without checking actual assertions.
  - Fix: run `pytest` and read the failure details before changing code.
- Mistake: forgetting to test edge cases like zero values and negative numbers.
  - Fix: add tests for boundary and special-case values.
- Mistake: not marking slow or expected-failure tests correctly.
  - Fix: use pytest markers like `@pytest.mark.slow`, `@pytest.mark.skip`, and `@pytest.mark.xfail` intentionally.

## Overall lessons

- Always validate code with tests after exercise work.
- Small mistakes are normal; the fix is often just understanding the logic more clearly.
- Keep a record of errors so the same mistakes are less likely to repeat.
- A good learner does not avoid mistakes; they learn from them and document the fix.
