# Example-to-send-an-email-with-fileConfig-of-Python-logging

This is a sample of sending an email with a Python logging fileConfig.

`sample.py` is the main body of the script.
`logging.conf` is the configuration file for logging.


```conf
[handler_emailHandler]
class=handlers.SMTPHandler
level=ERROR
formatter=emailFormatter
args=(('example.server.com', 465), 'from@example.com', ['to@example.com', ], 'ERROR!', ('username', 'password'), ())
```

To send mail, set `class` to `handlers.SMTPHandler`.

Send mail with `level=ERROR` for log levels above `ERROR`.

Set mail parameters in `args`.

* `'example.server.com'`: mailhost
* 465: PORT
* 'from@example.com': fromaddr
* `['to@example.com', ]`: toaddrs
* 'ERROR!': subject
* ('username', 'password'): credentials
* (): secure


[Official reference for SMTPHandler](https://docs.python.org/ja/3/library/logging.handlers.html#smtphandler)
