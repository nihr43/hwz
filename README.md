# hwz

A z-page for hardware.  Serves /healthz/ with the intent for metrics to be gathered by a larger system.

## justification

An alarming amount of enterprise monitoring solutions essentially operate with root ssh accounts.  This is a fundamentaly flawed approach as this establishes a 'god account' across the entire datacenter, and in my professional experience, this kind of thing never gets rotated.

By exposing a minimal set of metrics in simple json, we more closely adhere to the "least privilege" model; and we enable endless interfacing options.

The scope of this project is not large, and does not include performance metrics - there are numerous open source tools that solve this problem well.  Rather, i am focused on very basic hardware information - disk status, ECC errors, psu failure, etc.
