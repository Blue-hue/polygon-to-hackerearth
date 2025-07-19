# Polygon to HackerEarth Testcase Converter 🧪📦

This is a simple Python GUI application that converts testcases downloaded from [Polygon](https://polygon.codeforces.com/) into a HackerEarth-style format. Built using `tkinter`, it allows users to:

- Select a `.zip` file downloaded from Polygon.
- Choose an output folder.
- Automatically extract and repackage testcases in `inputXX.txt` / `outputXX.txt` format.
- Get a new `testcases.zip` ready for HackerEarth.

---

## 💻 Features

- GUI interface using `tkinter`
- Automatically names testcases as `input00.txt`, `output00.txt`, etc.
- Packs them into a `testcases.zip` inside the chosen folder
- Cross-platform support (Windows, Linux, macOS)
- Optional `.exe` build using `PyInstaller`

---

## 🏁 Getting Started

### ✅ Prerequisites

Make sure Python 3.7+ is installed. Then install dependencies: