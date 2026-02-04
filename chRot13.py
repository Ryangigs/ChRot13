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
    
    @staticmethod
    def init_colors(no_color: bool = False):
        """Initialize color support based on platform"""
        if no_color or not sys.stderr.isatty():
            Colors.HEADER = ''
            Colors.BLUE = ''
            Colors.GREEN = ''
            Colors.WARNING = ''
            Colors.FAIL = ''
            Colors.ENDC = ''
            Colors.BOLD = ''
            Colors.UNDERLINE = ''
            Colors.SUCCESS = ''
            Colors.ERROR = ''
            Colors.INFO = ''
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
                Colors.HEADER = ''
                Colors.BLUE = ''
                Colors.GREEN = ''
                Colors.WARNING = ''
                Colors.FAIL = ''
                Colors.ENDC = ''
                Colors.BOLD = ''
                Colors.UNDERLINE = ''
                Colors.SUCCESS = ''
                Colors.ERROR = ''
                Colors.INFO = ''
                return
        
        # Unix-like systems (Linux, macOS)
        Colors.HEADER = '\033[95m'
        Colors.BLUE = '\033[94m'
        Colors.GREEN = '\033[92m'
        Colors.WARNING = '\033[93m'
        Colors.FAIL = '\033[91m'
        Colors.ENDC = '\033[0m'
        Colors.BOLD = '\033[1m'
        Colors.UNDERLINE = '\033[4m'
        Colors.SUCCESS = '\033[92m'
        Colors.ERROR = '\033[91m'
        Colors.INFO = '\033[94m'


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