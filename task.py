# 1. 2 тооны нийлбэр
def check_addition(a, b):
    pass

# 2. 2 тооны ялгавар 
def check_subtraction(a, b):
    pass

# 3. 2 тооны үржвэр  
def check_multiplication(a, b):
    pass

# 4. 2 тооны хуваалт  
def check_division(a, b):
    pass

# 5. Квадрат (n^2)  
def check_square(n):
    pass

# 6. Куб (n^3)  
def check_cube(n):
    pass

# 7. Модуль (үлдэгдэл)  %
def check_modulus(a, b):
    pass

# 8. Зэрэг (power)  **
def check_power(base, exp):
    pass

# 9. 2 тооны дундаж утга 
def check_average(a, b):
    pass

# 10. Гурван тооны нийлбэр  
def check_sum_three(a, b, c):
    pass

# 11. Их тоог олох  
def check_max(a, b):
    pass

# 12. Бага тоог олох  
def check_min(a, b):
    pass

# 13. Тэгш эсэх  
def check_even(n):
    pass

# 14. Сондгой эсэх  
def check_odd(n):
    pass

# 15. Хувь (percentage)  
def check_percentage(part, whole):
    pass

# 16. Периметр (дөрвөлжин)  
def check_perimeter_square(side):
    pass

# 17. Талбай (дөрвөлжин)  
def check_area_square(side):
    pass

# 18. Талбай (тэгш өнцөгт)  
def check_area_rectangle(length, width):
    pass

# 19. Талбай (гурвалжин)  
def check_area_triangle(base, height):
    pass

def run_tests():
    test_cases = [
        (check_addition, (2, 3), 5),
        (check_subtraction, (5, 3), 2),
        (check_multiplication, (4, 3), 12),
        (check_division, (10, 2), 5),
        (check_square, (4,), 16),
        (check_cube, (3,), 27),
        (check_modulus, (10, 3), 1),
        (check_power, (2, 3), 8),
        (check_average, (4, 6), 5),
        (check_sum_three, (1, 2, 3), 6),
        (check_max, (10, 20), 20),
        (check_min, (10, 20), 10),
        (check_even, (4,), True),
        (check_odd, (5,), True),
        (check_percentage, (50, 200), 25),
        (check_perimeter_square, (4,), 16),
        (check_area_square, (5,), 25),
        (check_area_rectangle, (4, 6), 24),
        (check_area_triangle, (10, 2), 10),
    ]

    attempted = 0
    correct = 0

    for func, args, expected in test_cases:
        try:
            result = func(*args)

            if result is None:
                print(f"{func.__name__}: NOT ATTEMPTED")
                continue

            attempted += 1

            if isinstance(result, float):
                is_correct = abs(result - expected) < 1e-6
            else:
                is_correct = result == expected

            if is_correct:
                print(f"{func.__name__}: CORRECT")
                correct += 1
            else:
                print(f"{func.__name__}: WRONG (got {result} {expected})")

        except Exception as e:
            print(f"{func.__name__}: ERROR ({e})")

    print(f"\nAttempted: {attempted}/{len(test_cases)}")
    print(f"Correct: {correct}/{len(test_cases)}")
    
run_tests()