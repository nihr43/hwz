# hwz

A z-page for hardware.  Serves /healthz/ with the intent for metrics to be gathered by a larger system.

## justification

An alarming amount of enterprise monitoring solutions essentially operate with root ssh accounts.  This is a fundamentaly flawed approach as this establishes a 'god account' across the entire datacenter, and in my professional experience, this kind of thing never gets rotated.

By exposing a minimal set of metrics in simple json, we more closely adhere to the "least privilege" model; and we enable endless interfacing options.

The scope of this project is not large, and does not include performance metrics - there are numerous open source tools that solve this problem well.  Rather, i am focused on very basic hardware information - disk status, ECC errors, psu failure, etc.

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
