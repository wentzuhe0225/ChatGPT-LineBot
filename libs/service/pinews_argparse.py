from libs import configs
from argparse import ArgumentParser, RawTextHelpFormatter, ArgumentTypeError


class Args:
    def __init__(self) -> None:
        self.parser = ArgumentParser(
            description="The PiNews LineBot command line tool",
            formatter_class=RawTextHelpFormatter,
        )
        self.parser.add_argument(
            "-d",
            "--debug",
            type=self.str_to_bool,
            default=False,
            help="Debug function switch (default: False, you can use t/T/f/F/True/true/False/false to input)",
        )

    def str_to_bool(self, value: str | bool) -> bool:
        if isinstance(value, bool):
            return value
        elif value.lower() in ("true", "t"):
            return True
        elif value.lower() in ("false", "f"):
            return False
        else:
            raise ArgumentTypeError(f"Invalid boolean value: {value}")

    def debug_controller(self) -> None:
        args = self.parser.parse_args()
        configs.DEBUG = self.str_to_bool(args.debug)
