import re
#text = "My phone number is 408-555-1234"
#phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
#phone = re.search(r'\d{3}-\d{3}-\d{3}',text)
#print(phone)
#print(phone.group(3))
#print(phone.group())

#Additional Regex Syntax
#print(re.search(r'cat|dog','The cat is here')) 
#print(re.findall(r'at','The cat in the hat sat there.'))
#print(re.findall(r'.at','The cat in the hat sat there.'))
#print(re.findall(r'^\d','1 The cat in the hat sat there.'))
#print(re.findall(r'\d$','The cat in the hat sat there 2'))

#text = " Tanuj contact number is 9999999999, and its US contact number is (999)-333-7777"
#Extracting the both number
#pattern = r'\d{10}|\(\d{3}\)-\d{3}-\d{4}'
#matches = re.findall(pattern, text)
#print(matches)

text = '''NOTE 1 - Tesla was incorporated in July 2003 by Martin Eberhard and Marc Tarpenning as Tesla Motors. The company's name is a tribute to inventor and electrical engineer Nikola Tesla. In February 2004 Elon Musk joined as the company's largest shareholder and in 2008 he was named CEO. In 2008, the company began production of its first car model, the Roadster sports car, followed by the Model S sedan in 2012, the Model X SUV in 2015, the Model 3 sedan in 2017, the Model Y crossover in 2020, the Tesla Semi truck in 2022 and the Cybertruck pickup truck in 2023. The Model 3 is the all-time bestselling plug-in electric car worldwide, and in June 2021 became the first electric car to sell 1 million units globally.[6] In 2023, the Model Y was the best-selling vehicle, of any kind, globally.[3]

Tesla is one of the world's most valuable companies in terms of market capitalization. In October 2021, Tesla's market capitalization temporarily reached US$1 trillion, the sixth company to do so in U.S. history. In 2023, the company led the battery electric vehicle market, with 19.9% share. Also in 2023, the company was ranked 69th in the Forbes Global 2000.[7] As of March 2024, it is the world's most valuable automaker.

Tesla has been the subject of lawsuits, government scrutiny, and journalistic criticism, stemming from allegations of whistleblower retaliation, worker rights violations, product defects, and Musk's many controversial statements.

NOTE 2 - Tesla’s (TSLA) accounting policy has repeatedly come under review by the SEC (Securities and Exchange Commission) and analysts. In September, the SEC asked Tesla to comment on its costs on revenue, services, warranties, and its direct vehicle leasing program. In October, after Tesla’s reply, the SEC closed the review.

However, the issue resurfaced again after Tesla’s surprise profit in the third quarter. Most analysts were expecting a loss. The day after the earnings release, Tesla stock rose 17.7%. Barron’s and Wccftech have pointed out that the company reduced its warranted-related provisions and liabilities, which supported its profits.

Though analysts, media, and regulators have questioned Tesla’s accounting policies on various parameters, an area of contention has been its warranty expenses. Two main topics related to warranties have come under the radar.'''

pattern = r'NOTE \d'
matches = re.findall(pattern, text)
print(matches)
