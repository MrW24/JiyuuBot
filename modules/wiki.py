def wikipedia(self, string):
    import requests
    UA = "JiyuuBot/1 (http://github.com/JiyuuProject/JiyuuBot; bob@bob131.so) BasedOnRequests/%s" % requests.__version__
    matches = re.findall("(\w+).wikipedia.org/wiki/(\w+)", string)
    for match in matches:
        categories = requests.get("http://%s.wikipedia.org/w/api.php?action=query&prop=categories&format=json&cllimit=10&cldir=descending&titles=%s&redirects=" % match, headers={"user-agent": UA}).json()["query"]["pages"]
        categories = categories[categories.keys()[0]]
        if "missing" in categories.keys():
            self.conman.gen_send("Page not found")
        else:
            self.conman.gen_send("%s | Categories: %s" % (categories["title"].encode("utf-8"), ", ".join(re.sub("\w+:", "", x["title"].encode("utf-8")) for x in categories["categories"])))

self._map("regex", ".*\w+.wikipedia.org/wiki/\w+.*", wikipedia, "Wikipedia")