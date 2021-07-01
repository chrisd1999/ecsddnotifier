fields = [
    {
      "xpath": '//*[@id="goLogin"]/a',
      "method": 'click',
      "value": None,
    },
    {
        "xpath": '//*[@id="email"]',
        "method": 'send_keys',
        "value": 1,
    },
    {
        "xpath": '//*[@id="psw"]',
        "method": 'send_keys',
        "value": 1,
    },
    {
        "xpath": '//*[@id="doLogin"]',
        "method": 'click',
        "value": None,
    },
]

for field in fields:
    print(field['xpath'])