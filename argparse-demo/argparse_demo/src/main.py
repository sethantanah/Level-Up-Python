import argparse

def main():
    parser = argparse.ArgumentParser(description='Calculate the square of a number.')
    parser.add_argument('number', type=int, help='The number to square')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose output')
    
    args = parser.parse_args()
    
    result = args.number ** 2
    
    if args.verbose:
        print(f"The square of {args.number} is {result}")
    else:
        print(result)

# ARGUMENT TYPE
def argparse_argtype():
    """_summary_
    Argument Types: You can specify the type of argument (int, float, str, etc.) using the type parameter.
    """
    parser = argparse.ArgumentParser(description='Calculate the square of a number.')
    parser.add_argument('number', type=int, help='The number to square')
    
    args = parser.parse_args()
    
    result = args.number ** 2
    print(f"The square of {args.number} is {result}")

# DEFAULT VALUES
def argparse_default_values():
    """_summary_
    Default Values: You can set default values for arguments using the default parameter.
    """
    parser = argparse.ArgumentParser(description='Calculate the square of a number.')
    parser.add_argument('number', type=int, default=5, help='The number to square (default: 5)')
    
    args = parser.parse_args()
    
    result = args.number ** 2
    print(f"The square of {args.number} is {result}")

# HELP MESSAGES
def argparse_help_messages():
    """_summary_
   Help Messages: You can provide help messages for each argument using the help parameter.
    """
    parser = argparse.ArgumentParser(description='Calculate the square of a number.')
    parser.add_argument('number', type=int, help='The number to square')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose output')
    
    args = parser.parse_args()
    
    result = args.number ** 2
    
    if args.verbose:
        print(f"The square of {args.number} is {result}")
    else:
        print(result)

# ACTION
def argparse_action():
    """_summary_
    Action: You can specify what action should be taken when an argument 
    is encountered (e.g., store, store_true, store_false, append, etc.).
    """
    parser = argparse.ArgumentParser(description='Calculate the square of a number.')
    parser.add_argument('number', type=int, help='The number to square')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose output')
    
    args = parser.parse_args()
    
    result = args.number ** 2
    
    if args.verbose:
        print(f"The square of {args.number} is {result}")
    else:
        print(result)


# MUTUAL EXCLUSION
def argparse_mutual_exclusion():
    """_summary_
    Mutual Exclusion: You can define groups of arguments where only one can be 
    present using add_mutually_exclusive_group().
    """
    parser = argparse.ArgumentParser(description='Calculate the square of a number.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--square', action='store_true', help='Calculate the square of the number')
    group.add_argument('--cube', action='store_true', help='Calculate the cube of the number')
    parser.add_argument('number', type=int, help='The number')
    
    args = parser.parse_args()
    
    if args.square:
        result = args.number ** 2
        print(f"The square of {args.number} is {result}")
    elif args.cube:
        result = args.number ** 3
        print(f"The cube of {args.number} is {result}")
    else:
        print("Please specify either --square or --cube.")

# SUBPARSERS
def argparse_subparsers():
    """_summary_
    Subparsers: You can create subparsers using add_subparsers() 
    to define different command-line interfaces for different tasks.
    """
    parser = argparse.ArgumentParser(description='Calculate the square or cube of a number.')
    subparsers = parser.add_subparsers(dest='operation', help='Operation to perform')

    square_parser = subparsers.add_parser('square', help='Calculate the square of the number')
    square_parser.add_argument('number', type=int, help='The number')

    cube_parser = subparsers.add_parser('cube', help='Calculate the cube of the number')
    cube_parser.add_argument('number', type=int, help='The number')

    args = parser.parse_args()
    
    if args.operation == 'square':
        result = args.number ** 2
        print(f"The square of {args.number} is {result}")
    elif args.operation == 'cube':
        result = args.number ** 3
        print(f"The cube of {args.number} is {result}")
    else:
        print("Please specify an operation.")


if __name__ == "__main__":
    main()
