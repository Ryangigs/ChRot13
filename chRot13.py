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
    pass