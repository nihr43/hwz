# hwz

A healthz page for hardware.  Serves /healthz/ with the intent for metrics to be gathered by a larger system.

## scope

The scope of this project is to provide the simplest possible solution to harvest basic hardware information - disk status, ECC errors, psu failure, etc - from a large deployment of physical hardware.  There is decidedly no accounting/authentication.

## usage

Run the deamon:

```
$ python3 hwz.py
```

Query it as you wish:

```
$ curl -s 10.0.0.104:5000/healthz/ | jq
{
  "disks": [
    {
      "model": "SanDisk SD7TB3Q-256G-1006",
      "name": "sda",
      "reallocated_block_count": 0,
      "state": "WARN"
    },
    {
      "model": "SanDisk SD6SB1M-256G-1006",
      "name": "sdb",
      "reallocated_block_count": 0,
      "state": "PASS"
    }
  ]
}
```

Also see provided systemd unit example and requirements.txt
