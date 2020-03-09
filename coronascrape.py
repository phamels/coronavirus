import requests
import lxml.html as lh
import unidecode
import json

url = 'https://www.worldometers.info/coronavirus/'
output_file = 'covid19.json'

page = requests.get(url)
doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

col = []
i = 0
ret_data = {}


def switch_keys(keys):
    switcher = {
        "Country,Other": "Country",
        "TotalCases": "Total Cases",
        "NewCases": "New Cases",
        "TotalDeaths": "Total Deaths",
        "TotalRecovered": "Total Recovered",
        "ActiveCases": "Active Cases",
        "Serious,Critical": "Critical Cases",
    }
    return switcher.get(keys, "Invalid Key")


for t in tr_elements[0]:
    i += 1
    if not isinstance(t, lh.HtmlComment):
        name = t.text_content()
        col.append((name, []))

for j in range(1, len(tr_elements)):
    T = tr_elements[j]
    if len(T) != 12:
        break
    i = 0
    ret = {}
    country = None

    for t in T.iterchildren():
        if not isinstance(t, lh.HtmlComment):
            data = t.text_content().strip()
            if i == 0:
                country = data
                ret[country] = {}
            else:
                data = data.replace(',', '')
                try:
                    data = int(data)
                except:
                    pass
                try:
                    data = float(data)
                except:
                    pass
                if data == "":
                    data = 0.0
            unidecode.unidecode(col[i][0])
            ret[country][switch_keys(unidecode.unidecode(col[i][0]))] = data
            col[i][1].append(data)
            i += 1
    ret_data.update(ret)

with open(output_file, 'w') as f:
    f.write(json.dumps(ret_data))
