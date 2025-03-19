# lecture-spring-2025-Homework-1


Copyright 2025 Leopold Riedl

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is released under an MIT LICENSE.

This is the Homework-1 assignment for the lecture Open Source Energy System Modeling in Spring 2025.

This repository contains Python code for modeling the energy production of renewable energy sources, specifically solar and wind energy. The code includes functions to calculate the daily energy output from solar panels and wind turbines, based on parameters such as panel size, efficiency, wind speed, and blade length. Additionally, it computes the total energy production by combining the output from both sources.

The project uses Ruff as a code linter to ensure high code quality and maintainability. The configuration for Ruff is included in the pyproject.toml file, and a pre-commit hook is set up to automatically run the linter before each commit.

Unit tests are provided to verify the correctness of the functions, and pytest is used as the testing framework. The repository includes all necessary configurations to run the linter and tests, making it easy to maintain code quality and test coverage.
