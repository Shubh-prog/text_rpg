import sys
import time

def slow_print(text, delay=0.03):
    """
    Prints the text slowly, character by character.
    
    Args:
        text (str): The string to print.
        delay (float): Time delay between characters (seconds).
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to a new line at the end

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a,b = b, a+b
    return a