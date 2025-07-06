# AntarBhukti

**AntarBhukti** is a robust verification tool for evolving software, designed to analyze changes between two versions of Sequential Function Charts (SFCs)—a source and a target. It is purpose-built for use with OSCAT application benchmarks.

---

## 🚀 Features

- **SFC Comparison:** Accurately verifies software evolution using textual SFC representations.
- **Simple CLI:** Intuitive command-line interface for quick verification tasks.
- **Comprehensive Benchmarks:** Tested on all 80 OSCAT benchmark applications.<br>
  - `Benchmrak-Source-OSCAT.txt`: Contains 50 source/original SFCs.
    - ⚠️ **Input Formatting Required:**
      - Replace `"steps":` with `steps=`
      - Replace `"transitions":` with `transitions=`
      - Replace `"variables":` with `variables=`
      - Add: `initial_step="Init"`
  - `Benchmarks-Upgrade-OSCAT.txt`: Contains 50 upgraded/target SFCs.
    - Same formatting as `Benchmrak-Source-OSCAT.txt`.
- **Superior Performance:** Outperforms [verifaps](https://formal.kastel.kit.edu/~weigl/verifaps/index.html) in coverage and flexibility.
- **Open ST Reference:** Structured Text (ST) code for the OSCAT library is available at [www.oscat.de](https://www.oscat.de).

---

## 🧑‍💻 Getting Started

### Dependency Files

- `driver.py`
- `sfc.py`
- `sfc_verifier.py`
- `genreport.py`
- `iec61131.py`

### Prerequisites

- Python 3.x
- [Z3 SMT solver](https://github.com/Z3Prover/z3) (Python bindings)

---

## ⚡️ Usage

```sh
python3 driver.py <SFC-source.txt> <SFC-upgrade.txt>
```
- `<SFC-source.txt>`: Path to the source SFC file.
- `<SFC-upgrade.txt>`: Path to the upgraded (evolved) SFC file.

---

### Example

> **Note:** If your source and upgraded SFC files have different names, update the following lines in the code:

**In `driver.py` (lines 47 and 48):**
```python
sfc1.load("SFC-source.txt")  # Replace with your source filename
sfc2.load("SFC-upgrade.txt") # Replace with your upgrade filename
```
**In `sfc.py` (line 213):**
```python
sfc.load("SFC-source.txt")   # Replace with your source filename
```
**Then run:**
```sh
python3 driver.py <your_filename_source>.txt <your_filename_upgrade>.txt
```

**Current version example:**  
Run the tool on DEC to HEX converter:
```sh
python3 driver.py dec2hex.txt dec2hex_mod.txt
```

---

## 🏗️ OSCAT Benchmarks

AntarBhukti has been thoroughly tested on all 80 OSCAT automation benchmarks, ensuring robust and reliable verification.

---

## 📚 Reference

- For Structured Text (ST) code for the OSCAT library, check [www.oscat.de](https://www.oscat.de)

---

## 📄 License

MIT License

```
MIT License

Copyright (c) 2025 Soumyadip Bandyopadhyay

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgements

- Inspired by the need for robust SFC verification in industrial automation.
- Thanks to the OSCAT project and the verifaps tool for foundational ideas.
