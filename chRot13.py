#!/usr/bin/env python3
#  ____  _____  _    _  ____  ____  ____  ____     ____  _  _     ___  _   _  __  __  ___   ___  _  _ 
# (  _ \(  _  )( \/\/ )( ___)(  _ \( ___)(  _ \   (  _ \( \/ )   / __)( )_( )/. |/  )(__ \ / _ \( \( )
#  )___/ )(_)(  )    (  )__)  )   / )__)  )(_) )   ) _ < \  /   ( (__  ) _ ((_  _))(  / _/( (_) ))  ( 
# (__)  (_____)(__/\__)(____)(_)\_)(____)(____/   (____/ (__)    \___)(_) (_) (_)(__)(____)\___/(_)\_)
                        #################################################
                        # ChRot13 - Advanced ROT13 Encoder/Decoder Tool #
                        #################################################

import sys
import os
import argparse
import signal
import platform
from typing import Optional, TextIO


class Colors:
    """Cross-platform color handling"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    SUCCESS = '\033[92m'
    ERROR = '\033[91m'
    INFO = '\033[94m'

    @classmethod
    def init_colors(self, no_color: bool = False):
        """Initialize color support based on platform"""
        if no_color or not sys.stderr.isatty():
            self.HEADER = ''
            self.BLUE = ''
            self.GREEN = ''
            self.WARNING = ''
            self.FAIL = ''
            self.ENDC = ''
            self.BOLD = ''
            self.UNDERLINE = ''
            self.SUCCESS = ''
            self.ERROR = ''
            self.INFO = ''
            return
        
        system = platform.system()
        
        # Windows color support
        if system == "Windows":
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                # Fallback if Windows API fails
                self.HEADER = ''
                self.BLUE = ''
                self.GREEN = ''
                self.WARNING = ''
                self.FAIL = ''
                self.ENDC = ''
                self.BOLD = ''
                self.UNDERLINE = ''
                self.SUCCESS = ''
                self.ERROR = ''
                self.INFO = ''
                return
        
        # Unix-like systems (Linux, macOS)
        self.HEADER = '\033[95m'
        self.BLUE = '\033[94m'
        self.GREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.SUCCESS = '\033[92m'
        self.ERROR = '\033[91m'
        self.INFO = '\033[94m'


class Decorators:
    """Console decorators for status messages"""
    
    @staticmethod
    def success(msg: str, no_color: bool = False) -> str:
        if no_color:
            return f"[ + ] {msg}"
        return f"{Colors.SUCCESS}[ + ]{Colors.ENDC} {msg}"
    
    @staticmethod
    def error(msg: str, no_color: bool = False) -> str:
        if no_color:
            return f"[ ! ] {msg}"
        return f"{Colors.ERROR}[ ! ]{Colors.ENDC} {msg}"

    @staticmethod
    def info(msg: str, no_color: bool = False) -> str:
        if no_color:
            return f"[ - ] {msg}"
        return f"{Colors.INFO}[ - ]{Colors.ENDC} {msg}"

    @staticmethod
    def process(msg: str, no_color: bool = False) -> str:
        if no_color:
            return f"[ * ] {msg}"
        return f"{Colors.BLUE}[ * ]{Colors.ENDC} {msg}"

class ChRot13:
    """Main ROT13 processing class"""

    def __init__(self):
        self.version = "1.0.0"
        self.author = "Ch4120N"
        self.project = "ChRot13"
    
    def rot13_char(self, char: str) -> str:
        """Apply ROT13 transformation to a single character"""
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        return char

    def rot13(self, text: str, decode: bool = False, quiet: bool = False, no_color: bool = False) -> str:
        """
        Apply ROT13 to text
        Note: ROT13 is its own inverse, so encode and decode are the same
        """
        if not quiet:
            if decode:
                print(Decorators.process("Decoding ROT13...", no_color), file=sys.stderr)
            else:
                print(Decorators.process("Encoding ROT13...", no_color), file=sys.stderr)
        
        result = ''.join(self.rot13_char(char) for char in text)
        
        if not quiet:
            if decode:
                print(Decorators.success(f"Decoded {len(text)} characters", no_color), file=sys.stderr)
            else:
                print(Decorators.success(f"Encoded {len(text)} characters", no_color), file=sys.stderr)
        
        return result

    def process_file(self, filepath: str, decode: bool = False, output: Optional[str] = None, 
                     quiet: bool = False, verbose: bool = False, no_color: bool = False) -> None:
        """Process a file with ROT13"""
        try:
            if filepath == '-':
                # Read from stdin
                if verbose and not quiet:
                    print(Decorators.info("Reading from standard input...", no_color), file=sys.stderr)
                text = sys.stdin.read()
            else:
                if not os.path.exists(filepath):
                    print(Decorators.error(f"File not found: {filepath}", no_color), file=sys.stderr)
                    sys.exit(1)
                
                if verbose and not quiet:
                    print(Decorators.info(f"Processing file: {filepath}", no_color), file=sys.stderr)
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
            
            result = self.rot13(text, decode, quiet, no_color)
            
            if output:
                if verbose and not quiet:
                    print(Decorators.info(f"Writing output to: {output}", no_color), file=sys.stderr)
                with open(output, 'w', encoding='utf-8') as f:
                    f.write(result)
                if not quiet:
                    print(Decorators.success(f"Output written to {output}", no_color), file=sys.stderr)
            else:
                sys.stdout.write(result)
                
        except PermissionError:
            print(Decorators.error(f"Permission denied: {filepath}", no_color), file=sys.stderr)
            sys.exit(1)
        except UnicodeDecodeError:
            print(Decorators.error(f"File encoding error: {filepath}", no_color), file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(Decorators.error(f"Unexpected error: {str(e)}", no_color), file=sys.stderr)
            sys.exit(1)

    def process_text(self, text: str, decode: bool = False, output: Optional[str] = None,
                     quiet: bool = False, verbose: bool = False, no_color: bool = False) -> None:
        """Process direct text input"""
        if verbose and not quiet:
            print(Decorators.info("Processing text input...", no_color), file=sys.stderr)
        result = self.rot13(text, decode, quiet, no_color)
        
        if output:
            with open(output, 'w', encoding='utf-8') as f:
                f.write(result)
            if not quiet:
                print(Decorators.success(f"Output written to {output}", no_color), file=sys.stderr)
        else:
            sys.stdout.write(result)
    
    def show_banner(self, no_color: bool = False) -> None:
        """Display the tool banner with optional color support"""
        # Define color variables based on no_color flag
        color_prefix = '' if no_color else Colors.ERROR
        
        # Use triple-quoted string for better readability of the ASCII art
        banner_lines = [
            " ________  ___  ___  ________  ________  _________   _____  ________     ",
            "|\\   ____\\|\\  \\|\\  \\|\\   __  \\|\\   __  \\|\\___   ___\\/ __  \\|\\_____  \\    ",
            "\\ \\  \\___|\\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\|\\  \\|___ \\  \\_|\\/_|\\  \\|____|\\ /_   ",
            " \\ \\  \\    \\ \\   __  \\ \\   _  _\\ \\  \\\\\\  \\   \\ \\  \\\\|/ \\ \\  \\    \\|\\  \\  ",
            "  \\ \\  \\____\\ \\  \\ \\  \\ \\  \\\\  \\\\ \\  \\\\\\  \\   \\ \\  \\    \\ \\  \\  __\\_\\  \\ ",
            "   \\ \\_______\\ \\__\\ \\__\\ \\__\\\\ _\\\\ \\_______\\   \\ \\__\\    \\ \\__\\|\\_______\\",
            "    \\|_______|\\|__|\\|__|\\|__|\\|__|\\|_______|    \\|__|     \\|__|\\|_______|",
            ""  # Empty line for spacing
        ]
        
        # Apply color to each line and join
        colored_banner = '\n'.join(f"{color_prefix}{line}" for line in banner_lines)
        print(colored_banner, file=sys.stderr)


    def show_help(self, no_color: bool = False) -> None:
        """Display help information with optional color support"""
        
        # Define common text blocks
        usage_text = """USAGE:
        python chRot13.py [OPTIONS] [FILE/TEXT]"""
        
        examples_text = """EXAMPLES:
        Encode text:
            echo "Hello World" | python chRot13.py
            python chRot13.py -e "Hello World"
            python chRot13.py -e -f input.txt -o encoded.txt
        
        Decode text:
            echo "Uryyb Jbeyq" | python chRot13.py -d
            python chRot13.py -d "Uryyb Jbeyq"
            cat encoded.txt | python chRot13.py -d
        
        File operations:
            python chRot13.py -e -f input.txt
            python chRot13.py -d -f encoded.txt -o decoded.txt"""
        
        options_text = """OPTIONS:
        -h, --help          Show this help message
        -v, --version       Show version information
        -e, --encode        Encode text (default mode)
        -d, --decode        Decode text
        -f, --file FILE     Process a file
        -o, --output FILE   Write output to file
        -q, --quiet         Suppress all status messages
        -V, --verbose       Show detailed status messages
        -t, --text TEXT     Process direct text input
        --no-color          Disable colored output
        --banner            Show banner only"""
        
        notes_text = """NOTES:
        • ROT13 is its own inverse: encoding twice returns original text
        • Non-alphabetic characters are left unchanged
        • Can process files, stdin, or direct text input
        • Supports output redirection to files"""
        
        if no_color:
            help_text = f"""
    {usage_text}

    {examples_text}

    {options_text}

    {notes_text}
    """
        else:
            help_text = f"""
    {Colors.BOLD}{usage_text}{Colors.ENDC}

    {Colors.BOLD}EXAMPLES:{Colors.ENDC}
        {Colors.GREEN}Encode text:{Colors.ENDC}
            echo "Hello World" | python chRot13.py
            python chRot13.py -e "Hello World"
            python chRot13.py -e -f input.txt -o encoded.txt
        
        {Colors.GREEN}Decode text:{Colors.ENDC}
            echo "Uryyb Jbeyq" | python chRot13.py -d
            python chRot13.py -d "Uryyb Jbeyq"
            cat encoded.txt | python chRot13.py -d
        
        {Colors.GREEN}File operations:{Colors.ENDC}
            python chRot13.py -e -f input.txt
            python chRot13.py -d -f encoded.txt -o decoded.txt

    {Colors.BOLD}{options_text}{Colors.ENDC}

    {Colors.BOLD}{notes_text}{Colors.ENDC}
    """
        
        print(help_text, file=sys.stderr)

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print(f"\n{Decorators.info('Operation interrupted by user')}", file=sys.stderr)
    sys.exit(0)

if __name__ == "__main__":
    # Set up signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Create parser
    parser = argparse.ArgumentParser(
        description='ChRot13 - Advanced ROT13 Encoder/Decoder',
        add_help=False,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('-h', '--help', action='store_true', help='Show help message')
    parser.add_argument('-v', '--version', action='store_true', help='Show version')
    parser.add_argument('-e', '--encode', action='store_true', help='Encode text')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode text')
    parser.add_argument('-f', '--file', type=str, help='Input file (use - for stdin)')
    parser.add_argument('-o', '--output', type=str, help='Output file')
    parser.add_argument('-q', '--quiet', action='store_true', help='Suppress all status messages')
    parser.add_argument('-V', '--verbose', action='store_true', help='Show detailed status messages')
    parser.add_argument('-t', '--text', type=str, help='Text to process')
    parser.add_argument('--no-color', action='store_true', help='Disable colored output')
    parser.add_argument('--banner', action='store_true', help='Show banner only')
    
    # Parse arguments
    args, remaining = parser.parse_known_args()

    
    # Initialize colors based on arguments and platform
    Colors.init_colors(args.no_color)
    
    # Create ChRot13 instance
    tool = ChRot13()

    # Show banner if requested
    if args.banner:
        tool.show_banner(args.no_color)
        sys.exit(0)
    
    # Show version if requested
    if args.version:
        version_msg = f"ChRot13 v{tool.version} by {tool.author}"
        if not args.no_color:
            version_msg = f"{Colors.GREEN}ChRot13 v{tool.version}{Colors.ENDC} by {Colors.BLUE}{tool.author}{Colors.ENDC}"
        print(version_msg, file=sys.stderr)
        sys.exit(0)
    
    # Show help if requested or no arguments
    if args.help or (not args.file and not args.text and sys.stdin.isatty() and not remaining):
        tool.show_banner(args.no_color)
        tool.show_help(args.no_color)
        sys.exit(0)
    
    
    # Determine mode (default to encode)
    decode = args.decode
    encode = args.encode
    
    if decode and encode:
        print(Decorators.error("Cannot specify both --encode and --decode", args.no_color), file=sys.stderr)
        sys.exit(1)

    # Show banner for verbose mode
    if args.verbose and not args.quiet:
        tool.show_banner(args.no_color)


    # Process input
    try:
        if args.file:
            # Process file
            tool.process_file(args.file, decode, args.output, args.quiet, args.verbose, args.no_color)
        
        elif args.text:
            # Process direct text
            tool.process_text(args.text, decode, args.output, args.quiet, args.verbose, args.no_color)
        
        elif remaining:
            # Process text from positional arguments
            text = ' '.join(remaining)
            tool.process_text(text, decode, args.output, args.quiet, args.verbose, args.no_color)
        
        elif not sys.stdin.isatty():
            # Process from stdin
            tool.process_file('-', decode, args.output, args.quiet, args.verbose, args.no_color)
        
        else:
            # No input provided
            print(Decorators.error("No input provided", args.no_color), file=sys.stderr)
            tool.show_help(args.no_color)
            sys.exit(1)
            
    except KeyboardInterrupt:
        print(f"\n{Decorators.info('Operation cancelled', args.no_color)}", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(Decorators.error(f"Fatal error: {str(e)}", args.no_color), file=sys.stderr)
        sys.exit(1)