# trc-status

A python script that outputs the current count of completed recommendations from the Truth and Reconcilliation Commission's Calls to Action in JSON format.

You can add this script to a daily cron job that outputs to a file like so:

```
0 1 * * * /usr/bin/python3 PATH_TO_SCRIPT_DIRECTORY/trc-status.py
> PATH_TO_SCRIPT_DIRECTORY/trc-status.json
```

