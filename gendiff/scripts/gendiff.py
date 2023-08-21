import argparse

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', dest='FORMAT', help='set format of output')
    
    args = parser.parse_args()
    
if __name__ == "__main__":
    import sys
    if "-h" in sys.argv or "--help" in sys.argv:
        main()

