from mailin import Mailin

m = Mailin("https://api.sendinblue.com/v1.0","access key","secret key")
campaigns = m.get_campaigns('classic') # to retrieve all campaigns of type 'classic'
campaigns = m.get_campaigns('') # to retrieve all campaigns
