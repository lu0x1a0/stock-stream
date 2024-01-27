import dotenv

from awslambda import lambda_get_symbols_data_multi, lambda_check_symbols_info_multi

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read a string argument.")

    parser.add_argument("-e", "--env", type=str, help="env file", required=True)

    # Parse the command-line arguments
    args = parser.parse_args()

    if not dotenv.load_dotenv(args.env):
        raise Exception("environment file empty or not exist")

    event = {"time": "2024-01-27T08:12:00Z"}
    context = None
    lambda_get_symbols_data_multi(event, context)
    # lambda_check_symbols_info_multi(event, context)
