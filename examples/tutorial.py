from mailin import Mailin

m = Mailin("https://api.mailinblue.com/v1.0","access key","secret key")
campaigns = m.get_campaigns()
