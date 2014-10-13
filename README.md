CheckPrinter
============

Check that paper status of Stanford network printers by parsing the printer's admin page. Will only work on Stanford's internal network.

Setup:

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install BeautifulSoup`
4. Edit `printer.py` to change the URL of the printer
5. `chmod +x run.sh`
6. Run `run.sh` using a cron job
