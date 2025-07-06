# AntarBhukti

AntarBhukti is a verification tool for evolving software, designed to verify changes between two versions of SFCs (Sequential Function Charts) — a source and a target. It is specifically tailored for use with OSCAT application benchmarks.

---

## Features

- **Compare SFCs:** Verifies the correctness of software evolution using textual SFC representations.
- **Easy to Use:** Simple command line interface for fast verification tasks.
- **Benchmark Suite:** Works on all 80 OSCAT benchmark applications.  
  - `Benchmrak-Source-OSCAT.py` contains the source/original SFCs.  
  - `Benchmarks-Upgrade-OSCAT.py` contains the upgraded/target SFCs.
- **Superior Performance:** Outperforms [verifaps](https://formal.kastel.kit.edu/~weigl/verifaps/index.html) in coverage and flexibility.
- **Open ST Reference:** Reference ST code for the OSCAT library is available in the [SamaTulyata4PLC](https://github.com/soumyadipcsis/SamaTulyata4PLC) repository.

---

## Getting Started

**Dependency files:**  
- `driver.py`  
- `sfc.py`  
- `sfc_verifier.py`
- `genreport.py`
- `iec61131.py`

### Prerequisites

- Python 3.x
- [Z3 SMT solver](https://github.com/Z3Prover/z3) (Python bindings)

### Usage

```sh
python3 driver.py <SFC-source.txt> <SFC-upgrade.txt>
```
- `<SFC-source.txt>`: Path to the source SFC file.
- `<SFC-upgrade.txt>`: Path to the upgraded (evolved) SFC file.

### Example
For other examples if the file name of souce and upgraded SFC are different then the user need to change the following lines using the user wanted file name.
```sh
For driver.py line no 47 and 48
    sfc1.load("SFC-source.txt") #filename-1
    sfc2.load("SFC-upgrade.txt") #filename-2
For sfc.py line no 213
     sfc.load("SFC-source.txt")#filename-1
```sh
python3 driver.py sfc_old.txt sfc_new.txt
```

---

## OSCAT Benchmarks

AntarBhukti has been tested on all 80 OSCAT automation benchmarks for robust and reliable verification.

---

## Reference

- For Structured Text (ST) code for the OSCAT library, see the [SamaTulyata4PLC](https://github.com/soumyadipcsis/SamaTulyata4PLC) repository.

---

## License

MIT License

Copyright (c) 2025 soumyadipcsis

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

---

## Acknowledgements

- Inspired by the need for robust SFC verification in industrial automation.
- Thanks to the OSCAT project and the verifaps tool for foundational ideas.
