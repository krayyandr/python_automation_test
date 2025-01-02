def main():
    import argparse
    from scripts.example_script import run_example
    from scripts.sum_script import run_sum
    from utils.helpers import log_message

    parser = argparse.ArgumentParser(description="Python Automation Project")
    parser.add_argument('--run', type=str, help='Specify the script to run', required=True)
    
    args = parser.parse_args()

    if args.run == 'example':
        log_message("Running example script...")
        run_example()
    elif args.run == 'sum':
        log_message("Running sum script...")
        run_sum()
    else:
        log_message("Unknown script specified. Please use --run example.")

if __name__ == "__main__":
    main()