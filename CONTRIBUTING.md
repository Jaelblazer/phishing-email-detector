# Contributing to Phishing Email Detector

Thank you for your interest in contributing to our project! This document provides guidelines and steps for contributing.

## Table of Contents
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)

## Getting Started

1. **Fork the Repository**
   - Click the "Fork" button on the top right of the repository page
   - This creates a copy of the repository in your GitHub account

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/phishing-email-detector.git
   cd phishing-email-detector
   ```

3. **Set Up Development Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Development Process

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Write your code
   - Add tests
   - Update documentation

3. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

4. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select the appropriate branches
   - Fill in the PR template
   - Submit

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Keep functions small and focused
- Write docstrings for all functions

## Testing

- Write tests for new features
- Ensure all tests pass
- Update tests when modifying existing features
- Run tests before submitting PR:
  ```bash
  python -m pytest
  ```

## Documentation

- Update README.md for significant changes
- Add docstrings to new functions
- Update inline comments when modifying code
- Keep the documentation up-to-date

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the documentation
3. The PR must pass all CI checks
4. You may merge the PR once you have the sign-off of at least one other developer

## Need Help?

- Check the [Discussions](https://github.com/Jaelblazer/phishing-email-detector/discussions)
- Open an issue
- Contact the maintainers

Thank you for contributing! 🎉 