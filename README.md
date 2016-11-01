# unifi-tools
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

Miscellaneous tools for UniFi

## gen-minrssi.py
Set minrssi (seperate reprovision required):

```./gen-minrssi.py config.json bqp 20 > /opt/UniFi/sites/bqp/config.properties```

## countaps.py
Count how many APs you have of each type across all sites:

```./countaps.py config.json```

gets you:

```
U2O: 43
U7Ev2: 1
BZ2: 20
U2HSR: 7
Total: 71
```
