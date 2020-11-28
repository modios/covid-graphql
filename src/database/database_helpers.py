# Large file, try to directly load it form goolge link.
def fetchGoogleMobilityGlobal():
    url = "https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv"
    urllib.request.urlretrieve(url, "./data/all_countries/Google/Global_Mobility_Report.csv")