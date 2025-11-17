# MT300: Reduction Kinetics of a Spherical Pellet

## Overview
This repository contains the course assignment for MT300: Production of Iron and Ferro Alloys. The project compares reduction kinetics under chemical reaction control and diffusion control using the shrinking core model. The Python script computes the degree of reduction and plots the two model responses for normalized time.

## Repository contents
- `MT300_PIFA_ReductionKinetics_Assignment.pdf` - Final report with theory, equations, figures, and embedded code.
- `PIFA-ReductionKinetics.py` - Python script used to compute and plot the kinetics.
- `PLOT_F_VS_T.png` - Final plot image produced by the script.

## Quick start - run the code
1. Create a Python virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

2. Install dependencies
```bash
pip install numpy matplotlib
```

3. Run the script
```bash
python PIFA-ReductionKinetics.py
```

To save the plot:
```python
plt.savefig('output_plot.png', dpi=300, bbox_inches='tight')
```

## Description of the models implemented
Chemical reaction control:
$$F = 1 - (1 - t/\tau)^3$$

Diffusion control:
$$F = 1 - 3(1 - t/\tau)^2 + 2(1 - t/\tau)^3$$

## Expected output
- Interactive plot comparing the two mechanisms.
- The repository includes `PLOT_F_VS_T.png` as an example of the expected figure.

## Authors
- Anindith B. L. - 231MT008
- Shubhang S. Galagali - 231MT049
- Suhas Gowda M. - 231MT053

## Reference
Ahindra Ghosh and Amit Chatterjee, *Iron Making and Steelmaking: Theory and Practice*, PHI Learning.

## License
MIT License

Copyright (c) 2025 Shubhang S Galagali

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the Software), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
