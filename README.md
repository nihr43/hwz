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
      "model": "Crucial_CT275MX300SSD1",
      "name": "sda",
      "read_error_rate": 1081,
      "reallocated_block_count": 135,
      "state": "PASS",
      "temp": 36
    },
    {
      "model": "Crucial_CT275MX300SSD1",
      "name": "sdb",
      "read_error_rate": 1,
      "reallocated_block_count": 2,
      "state": "PASS",
      "temp": 40
    }
  ],
  "ecc": {
    "ecc_error_count": 0
  }
}
```

Also see provided systemd unit example and requirements.txt

## ansible role

An ansible role for debian is included.  To add to a project:

```
git -C roles/ submodule add https://github.com/nihr43/hwz.git
```
