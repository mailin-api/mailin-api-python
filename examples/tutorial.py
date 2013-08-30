from mailin import Mailin

m = Mailin("http://api-dev.mailin.fr","access key","secret key")
campaigns = m.get_campaigns()
