# this is real remove prefix 
# lsstrip not really remove prefix
links = [
        "www.b001.com",
        "www.youtube.com",
        "www.google.com",
        "www.wikipedia.com"
        ]

for link in links:
    print(link.removeprefix("www."))

