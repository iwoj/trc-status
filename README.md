# trc-status

A python script that outputs the current count of completed recommendations from the Truth and Reconcilliation Commission's Calls to Action in JSON format.

You can add this script to a daily cron job that outputs to a file like so:

```
0 1 * * * /usr/bin/python3 SCRIPT_DIR/trc-status.py > SCRIPT_DIR/trc-status.json
```

Replace `SCRIPT_DIR` with the path to this repository on your server.

Also includes a simple landing page for the data that refreshes constantly in
the background.

