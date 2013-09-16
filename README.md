# Mailin Python API

This is the Mailin python API wrapper. 

It currently supports all the API calls for v1.0. Each call returns an Object that is documented in our API docs, here are the objects.

 * Account
 * Campaign
 * Campaign statistics
 * Folder
 * List
 * Attribute
 * User
 * SMS
 * Process

### SMTP APIs

 * File
 * Mail
 * Bounces
 * Template
 * Report
 * Statistics
 * Webhooks

## Quickstart

1. You will need to first get the Access key and Secret key from [Mailinblue](https://www.mailinblue.com).

2. Assuming that you have cloned this git repo, or downloaded mailin.py . You can use this small sample script to get started
```python
from mailin import Mailin

m = Mailin("https://api.mailinblue.com/v1.0","access key","secret key")
campaigns = m.get_campaigns()
```
3. To explore more, you should visit the [Mailin API documentation](https://apidocs.mailinblue.com).
