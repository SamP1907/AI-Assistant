# https://www.google.com/search?q=weather+mumbai
# user agent - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
# span id - wob_tm  wob_dc

from requests_html import HTMLSession


def weather():
    s = HTMLSession()
    query = "mumbai"
    url = f"https://www.google.com/search?q=weather+{query}"
    r = s.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
    )

    # Fetch temperature
    temperature = r.html.find("span#wob_tm", first=True)
    if temperature:
        temperature = temperature.text

    else:
        temperature = "N/A"
        print("Temperature not found")

    # Fetch unit (handling absence gracefully)
    unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True)
    if unit:
        unit = unit.text
    else:
        unit = ""
        print("Unit not found")

    # Fetch description
    description = r.html.find("span#wob_dc", first=True)
    if description:
        description = description.text

    else:
        description = "N/A"
        print("Description not found")

    return temperature + " " + unit + " " + description


# Example usage
weather()
