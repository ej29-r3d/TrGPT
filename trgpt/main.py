import sys
import pkg_resources
from trgpt.translator import Translator

def print_help() -> None:
    """
    Prints the help message and exits the program.
    """

    print("Usage: trgpt [options] <phrase to translate>")
    print("Options:")
    print("  -h, --help             Show this help message and exit")
    print("  -l, --languages LANGUAGES")
    print("                         Specify target languages for translation. Format: <source_language>:<target_language1>,<target_language2>")
    sys.exit(0)


def main() -> None:
    """
    Main function to handle translation.
    """

    if len(sys.argv) < 2:
        print("Usage: trgpt <phrase to translate>")
        sys.exit(1)

    text_to_translate: str = ' '.join(sys.argv[1:])  # Joining the command-line arguments into a single string
    config_path: str = pkg_resources.resource_filename(__name__, 'config/config.yaml')  # Absolute path to the config file within the package
    translator: Translator = Translator(config_path=config_path)  # Initializing the Translator with the config file path
    translations: dict[str, str] = translator.translate(text_to_translate)  # Getting translations


    print(translations)                                                         # Printing the translations

if __name__ == '__main__':
    main()
