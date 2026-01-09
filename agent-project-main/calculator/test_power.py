#!/usr/bin/env python3
# Quick test for the new power function

from pkg.calculator import Calculator

def test_power():
    calc = Calculator()
    
    # Test basic power operations
    test_cases = [
        ("2 ** 3", 8.0),      # 2^3 = 8
        ("3 ** 2", 9.0),      # 3^2 = 9
        ("5 ** 0", 1.0),      # 5^0 = 1
        ("2 ** 4", 16.0),     # 2^4 = 16
        ("10 ** 2", 100.0),   # 10^2 = 100
    ]
    
    print("Testing power function:")
    for expression, expected in test_cases:
        result = calc.evaluate(expression)
        print(f"{expression} = {result} (expected: {expected})")
        assert result == expected, f"Failed: {expression} returned {result}, expected {expected}"
    
    # Test power with other operations (precedence)
    result = calc.evaluate("2 + 3 ** 2")  # Should be 2 + 9 = 11
    print(f"2 + 3 ** 2 = {result} (expected: 11.0)")
    assert result == 11.0, f"Precedence test failed: got {result}, expected 11.0"
    
    result = calc.evaluate("2 * 3 ** 2")  # Should be 2 * 9 = 18
    print(f"2 * 3 ** 2 = {result} (expected: 18.0)")
    assert result == 18.0, f"Precedence test failed: got {result}, expected 18.0"
    
    print("\nAll power function tests passed!")

if __name__ == "__main__":
    test_power()