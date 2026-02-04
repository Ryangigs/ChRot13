

<div align='center'>

# ChRot13 - Advanced ROT13 Encoder/Decoder Tool

![Version](https://img.shields.io/badge/Version-1.1.0-green)
![LICENSE](https://img.shields.io/badge/License-GPLv3-orange)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey)

`ChRot13` is a powerful, cross-platform ROT13 encoding/decoding tool with beautiful UI and extensive features. ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet. It's its own inverse - encoding twice returns the original text.

</div>

---
## 👨‍💻 Project Programmer
> Ch4120N — [Ch4120N@Proton.me](mailto:Ch4120N@Proton.me)
---
## 🖼️ Screenshots

---
## 💻 Supported Platforms

* **Linux** (All distributions)
* **Windows** (7, 8, 10, 11)
* **macOS** (All versions)

---

## ✨ Features
* **Cross-platform**: Works on Windows, Linux, and macOS
* **Multiple input methods**: Files, stdin, or direct text input
* **Flexible output**: Terminal, files, or pipes
* **Beautiful UI**: Colored output with banners and status messages
* **Verbose/Quiet modes**: Control output verbosity
* **No-color mode**: For scripts and terminals without color support
* **Error handling**: Robust error handling with clear messages
* **Signal handling**: Graceful Ctrl+C handling

---
## 📋 Requirements
* Python 3.6 or higher
* No external dependencies required
---
## 🚀 Installation
### **Method 1: Direct Download**
```bash
# Download the script
curl -O https://raw.githubusercontent.com/Ch4120N/ChRot13/main/chRot13.py

# Make executable (Linux/macOS)
chmod +x chRot13.py
```

### **Method 2: Clone Repository**
```bash
git clone https://github.com/Ch4120N/ChRot13.git
cd ChRot13/
```
---
## 📖 Usage
### **Basic Examples**
```bash
# Encode text
python chRot13.py "Hello World"

# Decode text
python chRot13.py -d "Uryyb Jbeyq"

# Encode file
python chRot13.py -f input.txt

# Decode file with output
python chRot13.py -d -f encoded.txt -o decoded.txt

# Pipe input
echo "Hello" | python chRot13.py
cat file.txt | python chRot13.py -d

# Direct text input
python chRot13.py --text "Secret Message"
```

### **Advanced Examples**
```bash
# Show banner only
python chRot13.py --banner

# Verbose mode with banner
python chRot13.py --verbose -e "Hello World"

# Quiet mode (suppress all status messages)
python chRot13.py --quiet -f secret.txt -o encoded.txt

# No-color output (for scripts)
python chRot13.py --no-color "Hello World"

# Combine options
python chRot13.py --verbose --no-color -d -f encoded.txt -o decoded.txt
```
---
## 🛠️ Command Line Options
| Option | Description |
|--------|-------------|
| `-h`, `--help` | Show help message| |
| `-v`, `--version` | Show version information |
| `-e`, `--encode` | Encode text (default mode) |
| `-d`, `--decode` | Decode text |
| `-f`, `--file FILE` | Process a file (use - for stdin) |
| `-o`, `--output FILE`	| Write output to file |
| `-t`, `--text TEXT` | Process direct text input |
| `-q`, `--quiet` | Suppress all status messages |
| `-V`, `--verbose` | Show detailed status messages |
| `--no-color` | Disable colored output |
| `--banner` | Show banner only |
---
## 🔧 Advanced Features
### Color Support
* **Linux/macOS**: ANSI escape codes
* **Windows**: Windows API for color support (Windows 7+)
* **Automatic detection**: Disables colors when piping or redirected

### Error Handling
* File not found errors
* Permission errors
* Unicode encoding errors
* Graceful Ctrl+C handling

### Performance
* Memory efficient for large files
* Stream processing for stdin
* Fast character transformation
---
## 🐛 Troubleshooting

| **Issue** | **Solution** |
|-----------|--------------|
| Colors not working on Windows | Ensure you're running on Windows 10+ or use `--no-color` |
| 
| Permission denied when writing files | Check file permissions or run as administrator |
| Unicode errors with files | Files are read as **UTF-8**, ensure correct encoding |
| Script not executable | Run with `python chRot13.py` or make executable with `chmod +x` |
---
## ❤️ Support the Project
If you find this tool useful, consider donating:

| **Cryptocurrency** | **Address** |
|--------------------|-------------|
| **BTC** | `bc1ql4syps7qpa3djqrxwht3g66tldyh4j7qsyjkq0` |
| **ETH** | `0xfddbd535a4ad28792cbebceee3d6982d774e6d13` |
| **USDT** | `3Cq6HRQsiwZFmPEQfG9eJkZE2QGChvf2VN` |

> 💖 Your support helps keep the project alive and improving!


---
## ⚠️ Disclaimer
**This tool is for educational and authorized security testing purposes only.**

* ⚠️ **Unauthorized access to computer systems is illegal**
* ⚠️ **Only use this tool on systems you own or have explicit written permission to test**
* ⚠️ **The authors are not responsible for any misuse of this software**
* ⚠️ **Use responsibly and in compliance with applicable laws**

**By using this tool, you agree to use it only for legitimate security testing and educational purposes.**

---
## 🚨 Reporting Issues
> If you encounter bugs, configuration issues, or unexpected behavior, please reach out: 📩 [Ch4120N@Proton.me](mailto:Ch4120N@Proton.me) or use Issues in this repository

---

<div align='center'>

**⭐ If you like this project, don't forget to give it a star!**

Made with ❤️ by Ch4120N

</div>