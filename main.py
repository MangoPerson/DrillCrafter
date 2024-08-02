from parsers import parse_drill_set
from plotting import plot_set


def main():
    set_str = """
    S1 DOT 1.5<50, 12 ^ HS
    Q1 DOT 1.5>50, 12 ^ HS
    D(4...1) LINE 3.5 < 50, 13 v HH TO 3.5 > 50, 13 v HH
    
    M(1...5) LINE 2 < L40, 10 v HH TO 4 < 50, 10 v HH
    C(1,3,2) F(2,1) LINE 2 > R40, 10 v HH TO 4>50, 10 v HH
    """
    first_set = parse_drill_set(8, set_str)
    plot_set(first_set)


if __name__ == '__main__':
    main()
