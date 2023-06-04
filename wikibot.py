import wikipedia as wk

def scrape(name="Barack", lenght=1):
    result = wk.summary(name, sentences=lenght)
    return result

print(scrape("Microsoft"))