# trc-status

Track Canada's reconciliation process with this (very slowly) updating live
progress bar. Works well on computer store web browsers, library kiosks, and
just about any public video screen. Leave it running for a few years.

https://trcprogressbar.ca

## Components

A python script that outputs the current count of completed recommendations from the Truth and Reconcilliation Commission's Calls to Action in JSON format.

You can add this script to a daily cron job that outputs to a file like so:

```
0 1 * * * /usr/bin/python3 SCRIPT_DIR/trc-status.py > SCRIPT_DIR/trc-status.json
```

Replace `SCRIPT_DIR` with the path to this repository on your server.

Also includes a simple landing page for the data that refreshes data constantly in
the background.

