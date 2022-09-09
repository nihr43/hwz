# hwz

A z-page for hardware.  Serves /healthz/ with the intent for metrics to be gathered by a larger system.

## justification

An alarming amount of 'enterprise' monitoring solutions essentially involve either A: shell scripts executed over root ssh accounts or B: mystery binaries running as root provided by a paid vendor.  This is a fundamentaly flawed approach as this establishes yet another 'god account' across the entire datacenter.

By exposing a minimal set of metrics over http, we more closely adhere to the "least privilege" model; and we enable limitless interfacing options.  This is not a novel idea.

The scope of this project is not large, and does not include performance metrics - there are numerous open source tools that better solve that problem.  Rather, i am focused on very basic hardware information - disk status, ECC errors, psu failure, etc - the kinds of things where yes - ECC memory, modern fault tolerant storage, or a redundant power source may handle the initial problem, but i still need a simple way to actually find and address issues in a sea of hardware.  ( emphasis on simple; i simply dont feel like installing, configuring, and maintaining something like zabbix. )

There is intentionally no accounting/authentication.  While im sure someone somewhere can come up with an edge-case reason why they do not want their LAN to know their smart stats, this is not a threat channel i am going to spend my time on.  My bigger concern would be the authenticity/security of the libraries being imported.

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
