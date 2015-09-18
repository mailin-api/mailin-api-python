from mailin import Mailin

m = Mailin("https://api.sendinblue.com/v2.0","access key")

# to retrieve all campaigns of type 'classic' & status 'queued'
data = { "type":"classic",
	"status":"queued",
	"page":1,
	"page_limit":10
}

campaigns = m.get_campaigns_v2(data)