Overview
========

Usage
-----

    py pine_script_pdf.py

Produces an `error.log`.

Purpose
-------
TradingView does not provide PDF manuals for Pine Script. This is an attempt to
scrape <https://www.tradingview.com/pine-script-docs/index.html>.

Written in about 1 hour by GPT-4 Turbo.

Prerequisites
=============

Python
------

First version written with: Python 3.13.2

wkhtmltopdf
-----------

Requires wkhtmltopdf <https://wkhtmltopdf.org/>.
No need to install it with admin rights on Windows.

###  Manual Use of wkhtmltopdf
```
'/c/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'  https://www.tradingview.com/pine-script-docs/primer/first-steps first-steps.pdf
```
