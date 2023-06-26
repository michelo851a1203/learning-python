# lsstrip is the method that provide to strip characters include in method
links = [
        "www.b001.io",
        "www.youtube.com",
        "www.google.com",
        "www.wikipedia.org"
        ]

for link in links:
    # this will see wikipedia , w is rmeoved
    print(link.lstrip("www."))

print("======================")

# the same as "www."
for link in links:
    print(link.lstrip("w."))
