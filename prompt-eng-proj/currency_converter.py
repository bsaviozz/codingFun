import requests

codes = ['AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']
currency_names = [
    {"currency": "Afghan Afghani", "code": "AFN"},
    {"currency": "Albanian Lek", "code": "ALL"},
    {"currency": "Armenian Dram", "code": "AMD"},
    {"currency": "Netherlands Antillian Guilder", "code": "ANG"},
    {"currency": "Angolan Kwanza", "code": "AOA"},
    {"currency": "Argentine Peso", "code": "ARS"},
    {"currency": "Australian Dollar", "code": "AUD"},
    {"currency": "Aruban Florin", "code": "AWG"},
    {"currency": "Azerbaijani Manat", "code": "AZN"},
    {"currency": "Bosnia and Herzegovina Mark", "code": "BAM"},
    {"currency": "Barbados Dollar", "code": "BBD"},
    {"currency": "Bangladeshi Taka", "code": "BDT"},
    {"currency": "Bulgarian Lev", "code": "BGN"},
    {"currency": "Bahraini Dinar", "code": "BHD"},
    {"currency": "Burundian Franc", "code": "BIF"},
    {"currency": "Bermudian Dollar", "code": "BMD"},
    {"currency": "Brunei Dollar", "code": "BND"},
    {"currency": "Bolivian Boliviano", "code": "BOB"},
    {"currency": "Brazilian Real", "code": "BRL"},
    {"currency": "Bahamian Dollar", "code": "BSD"},
    {"currency": "Bhutanese Ngultrum", "code": "BTN"},
    {"currency": "Botswana Pula", "code": "BWP"},
    {"currency": "Belarusian Ruble", "code": "BYN"},
    {"currency": "Belize Dollar", "code": "BZD"},
    {"currency": "Canadian Dollar", "code": "CAD"},
    {"currency": "Congolese Franc", "code": "CDF"},
    {"currency": "Swiss Franc", "code": "CHF"},
    {"currency": "Chilean Peso", "code": "CLP"},
    {"currency": "Chinese Renminbi", "code": "CNY"},
    {"currency": "Colombian Peso", "code": "COP"},
    {"currency": "Costa Rican Colon", "code": "CRC"},
    {"currency": "Cuban Peso", "code": "CUP"},
    {"currency": "Cape Verdean Escudo", "code": "CVE"},
    {"currency": "Czech Koruna", "code": "CZK"},
    {"currency": "Djiboutian Franc", "code": "DJF"},
    {"currency": "Danish Krone", "code": "DKK"},
    {"currency": "Dominican Peso", "code": "DOP"},
    {"currency": "Algerian Dinar", "code": "DZD"},
    {"currency": "Egyptian Pound", "code": "EGP"},
    {"currency": "Eritrean Nakfa", "code": "ERN"},
    {"currency": "Ethiopian Birr", "code": "ETB"},
    {"currency": "Euro", "code": "EUR"},
    {"currency": "Fiji Dollar", "code": "FJD"},
    {"currency": "Falkland Islands Pound", "code": "FKP"},
    {"currency": "Faroese Króna", "code": "FOK"},
    {"currency": "Pound Sterling", "code": "GBP"},
    {"currency": "Georgian Lari", "code": "GEL"},
    {"currency": "Guernsey Pound", "code": "GGP"},
    {"currency": "Ghanaian Cedi", "code": "GHS"},
    {"currency": "Gibraltar Pound", "code": "GIP"},
    {"currency": "Gambian Dalasi", "code": "GMD"},
    {"currency": "Guinean Franc", "code": "GNF"},
    {"currency": "Guatemalan Quetzal", "code": "GTQ"},
    {"currency": "Guyanese Dollar", "code": "GYD"},
    {"currency": "Hong Kong Dollar", "code": "HKD"},
    {"currency": "Honduran Lempira", "code": "HNL"},
    {"currency": "Croatian Kuna", "code": "HRK"},
    {"currency": "Haitian Gourde", "code": "HTG"},
    {"currency": "Hungarian Forint", "code": "HUF"},
    {"currency": "Indonesian Rupiah", "code": "IDR"},
    {"currency": "Israeli New Shekel", "code": "ILS"},
    {"currency": "Manx Pound", "code": "IMP"},
    {"currency": "Indian Rupee", "code": "INR"},
    {"currency": "Iraqi Dinar", "code": "IQD"},
    {"currency": "Iranian Rial", "code": "IRR"},
    {"currency": "Icelandic Króna", "code": "ISK"},
    {"currency": "Jersey Pound", "code": "JEP"},
    {"currency": "Jamaican Dollar", "code": "JMD"},
    {"currency": "Jordanian Dinar", "code": "JOD"},
    {"currency": "Japanese Yen", "code": "JPY"},
    {"currency": "Kenyan Shilling", "code": "KES"},
    {"currency": "Kyrgyzstani Som", "code": "KGS"},
    {"currency": "Cambodian Riel", "code": "KHR"},
    {"currency": "Kiribati Dollar", "code": "KID"},
    {"currency": "Comorian Franc", "code": "KMF"},
    {"currency": "South Korean Won", "code": "KRW"},
    {"currency": "Kuwaiti Dinar", "code": "KWD"},
    {"currency": "Cayman Islands Dollar", "code": "KYD"},
    {"currency": "Kazakhstani Tenge", "code": "KZT"},
    {"currency": "Lao Kip", "code": "LAK"},
    {"currency": "Lebanese Pound", "code": "LBP"},
    {"currency": "Sri Lanka Rupee", "code": "LKR"},
    {"currency": "Liberian Dollar", "code": "LRD"},
    {"currency": "Lesotho Loti", "code": "LSL"},
    {"currency": "Libyan Dinar", "code": "LYD"},
    {"currency": "Moroccan Dirham", "code": "MAD"},
    {"currency": "Moldovan Leu", "code": "MDL"},
    {"currency": "Malagasy Ariary", "code": "MGA"},
    {"currency": "Macedonian Denar", "code": "MKD"},
    {"currency": "Burmese Kyat", "code": "MMK"},
    {"currency": "Mongolian Tögrög", "code": "MNT"},
    {"currency": "Macanese Pataca", "code": "MOP"},
    {"currency": "Mauritanian Ouguiya", "code": "MRU"},
    {"currency": "Mauritian Rupee", "code": "MUR"},
    {"currency": "Maldivian Rufiyaa", "code": "MVR"},
    {"currency": "Malawian Kwacha", "code": "MWK"},
    {"currency": "Mexican Peso", "code": "MXN"},
    {"currency": "Malaysian Ringgit", "code": "MYR"},
    {"currency": "Mozambican Metical", "code": "MZN"},
    {"currency": "Namibian Dollar", "code": "NAD"},
    {"currency": "Nigerian Naira", "code": "NGN"},
    {"currency": "Nicaraguan Córdoba", "code": "NIO"},
    {"currency": "Norwegian Krone", "code": "NOK"},
    {"currency": "Nepalese Rupee", "code": "NPR"},
    {"currency": "New Zealand Dollar", "code": "NZD"},
    {"currency": "Omani Rial", "code": "OMR"},
    {"currency": "Panamanian Balboa", "code": "PAB"},
    {"currency": "Peruvian Sol", "code": "PEN"},
    {"currency": "Papua New Guinean Kina", "code": "PGK"},
    {"currency": "Philippine Peso", "code": "PHP"},
    {"currency": "Pakistani Rupee", "code": "PKR"},
    {"currency": "Polish Złoty", "code": "PLN"},
    {"currency": "Paraguayan Guaraní", "code": "PYG"},
    {"currency": "Qatari Riyal", "code": "QAR"},
    {"currency": "Romanian Leu", "code": "RON"},
    {"currency": "Serbian Dinar", "code": "RSD"},
    {"currency": "Russian Ruble", "code": "RUB"},
    {"currency": "Rwandan Franc", "code": "RWF"},
    {"currency": "Saudi Riyal", "code": "SAR"},
    {"currency": "Solomon Islands Dollar", "code": "SBD"},
    {"currency": "Seychellois Rupee", "code": "SCR"},
    {"currency": "Sudanese Pound", "code": "SDG"},
    {"currency": "Swedish Krona", "code": "SEK"},
    {"currency": "Singapore Dollar", "code": "SGD"},
    {"currency": "Saint Helena Pound", "code": "SHP"},
    {"currency": "Sierra Leonean Leone", "code": "SLE"},
    {"currency": "Somali Shilling", "code": "SOS"},
    {"currency": "Surinamese Dollar", "code": "SRD"},
    {"currency": "South Sudanese Pound", "code": "SSP"},
    {"currency": "São Tomé and Príncipe Dobra", "code": "STN"},
    {"currency": "Syrian Pound", "code": "SYP"},
    {"currency": "Eswatini Lilangeni", "code": "SZL"},
    {"currency": "Thai Baht", "code": "THB"},
    {"currency": "Tajikistani Somoni", "code": "TJS"},
    {"currency": "Turkmenistan Manat", "code": "TMT"},
    {"currency": "Tunisian Dinar", "code": "TND"},
    {"currency": "Tongan Paʻanga", "code": "TOP"},
    {"currency": "Turkish Lira", "code": "TRY"},
    {"currency": "Trinidad and Tobago Dollar", "code": "TTD"},
    {"currency": "Tuvaluan Dollar", "code": "TVD"},
    {"currency": "New Taiwan Dollar", "code": "TWD"},
    {"currency": "Tanzanian Shilling", "code": "TZS"},
    {"currency": "Ukrainian Hryvnia", "code": "UAH"},
    {"currency": "Ugandan Shilling", "code": "UGX"},
    {"currency": "United States Dollar", "code": "USD"},
    {"currency": "Uruguayan Peso", "code": "UYU"},
    {"currency": "Uzbekistani So'm", "code": "UZS"},
    {"currency": "Venezuelan Bolívar Soberano", "code": "VES"},
    {"currency": "Vietnamese Đồng", "code": "VND"},
    {"currency": "Vanuatu Vatu", "code": "VUV"},
    {"currency": "Samoan Tālā", "code": "WST"},
    {"currency": "Central African CFA Franc", "code": "XAF"},
    {"currency": "East Caribbean Dollar", "code": "XCD"},
    {"currency": "Special Drawing Rights", "code": "XDR"},
    {"currency": "West African CFA franc", "code": "XOF"},
    {"currency": "CFP Franc", "code": "XPF"},
    {"currency": "Yemeni Rial", "code": "YER"},
    {"currency": "South African Rand", "code": "ZAR"},
    {"currency": "Zambian Kwacha", "code": "ZMW"},
    {"currency": "Zimbabwean Dollar", "code": "ZWL"}
]
country_names = [
    {"country": "Afghanistan", "code": "AFN"},
    {"country": "Albania", "code": "ALL"},
    {"country": "Armenia", "code": "AMD"},
    {"country": "Netherlands Antilles", "code": "ANG"},
    {"country": "Angola", "code": "AOA"},
    {"country": "Argentina", "code": "ARS"},
    {"country": "Australia", "code": "AUD"},
    {"country": "Aruba", "code": "AWG"},
    {"country": "Azerbaijan", "code": "AZN"},
    {"country": "Bosnia and Herzegovina", "code": "BAM"},
    {"country": "Barbados", "code": "BBD"},
    {"country": "Bangladesh", "code": "BDT"},
    {"country": "Bulgaria", "code": "BGN"},
    {"country": "Bahrain", "code": "BHD"},
    {"country": "Burundi", "code": "BIF"},
    {"country": "Bermuda", "code": "BMD"},
    {"country": "Brunei", "code": "BND"},
    {"country": "Bolivia", "code": "BOB"},
    {"country": "Brazil", "code": "BRL"},
    {"country": "Bahamas", "code": "BSD"},
    {"country": "Bhutan", "code": "BTN"},
    {"country": "Botswana", "code": "BWP"},
    {"country": "Belarus", "code": "BYN"},
    {"country": "Belize", "code": "BZD"},
    {"country": "Canada", "code": "CAD"},
    {"country": "Democratic Republic of the Congo", "code": "CDF"},
    {"country": "Switzerland", "code": "CHF"},
    {"country": "Chile", "code": "CLP"},
    {"country": "China", "code": "CNY"},
    {"country": "Colombia", "code": "COP"},
    {"country": "Costa Rica", "code": "CRC"},
    {"country": "Cuba", "code": "CUP"},
    {"country": "Cape Verde", "code": "CVE"},
    {"country": "Czech Republic", "code": "CZK"},
    {"country": "Djibouti", "code": "DJF"},
    {"country": "Denmark", "code": "DKK"},
    {"country": "Dominican Republic", "code": "DOP"},
    {"country": "Algeria", "code": "DZD"},
    {"country": "Egypt", "code": "EGP"},
    {"country": "Eritrea", "code": "ERN"},
    {"country": "Ethiopia", "code": "ETB"},
    {"country": "European Union", "code": "EUR"},
    {"country": "Fiji", "code": "FJD"},
    {"country": "Falkland Islands", "code": "FKP"},
    {"country": "Faroe Islands", "code": "FOK"},
    {"country": "United Kingdom", "code": "GBP"},
    {"country": "Georgia", "code": "GEL"},
    {"country": "Guernsey", "code": "GGP"},
    {"country": "Ghana", "code": "GHS"},
    {"country": "Gibraltar", "code": "GIP"},
    {"country": "The Gambia", "code": "GMD"},
    {"country": "Guinea", "code": "GNF"},
    {"country": "Guatemala", "code": "GTQ"},
    {"country": "Guyana", "code": "GYD"},
    {"country": "Hong Kong", "code": "HKD"},
    {"country": "Honduras", "code": "HNL"},
    {"country": "Croatia", "code": "HRK"},
    {"country": "Haiti", "code": "HTG"},
    {"country": "Hungary", "code": "HUF"},
    {"country": "Indonesia", "code": "IDR"},
    {"country": "Israel", "code": "ILS"},
    {"country": "Isle of Man", "code": "IMP"},
    {"country": "India", "code": "INR"},
    {"country": "Iraq", "code": "IQD"},
    {"country": "Iran", "code": "IRR"},
    {"country": "Iceland", "code": "ISK"},
    {"country": "Jersey", "code": "JEP"},
    {"country": "Jamaica", "code": "JMD"},
    {"country": "Jordan", "code": "JOD"},
    {"country": "Japan", "code": "JPY"},
    {"country": "Kenya", "code": "KES"},
    {"country": "Kyrgyzstan", "code": "KGS"},
    {"country": "Cambodia", "code": "KHR"},
    {"country": "Kiribati", "code": "KID"},
    {"country": "Comoros", "code": "KMF"},
    {"country": "South Korea", "code": "KRW"},
    {"country": "Kuwait", "code": "KWD"},
    {"country": "Cayman Islands", "code": "KYD"},
    {"country": "Kazakhstan", "code": "KZT"},
    {"country": "Laos", "code": "LAK"},
    {"country": "Lebanon", "code": "LBP"},
    {"country": "Sri Lanka", "code": "LKR"},
    {"country": "Liberia", "code": "LRD"},
    {"country": "Lesotho", "code": "LSL"},
    {"country": "Libya", "code": "LYD"},
    {"country": "Morocco", "code": "MAD"},
    {"country": "Moldova", "code": "MDL"},
    {"country": "Madagascar", "code": "MGA"},
    {"country": "North Macedonia", "code": "MKD"},
    {"country": "Myanmar", "code": "MMK"},
    {"country": "Mongolia", "code": "MNT"},
    {"country": "Macau", "code": "MOP"},
    {"country": "Mauritania", "code": "MRU"},
    {"country": "Mauritius", "code": "MUR"},
    {"country": "Maldives", "code": "MVR"},
    {"country": "Malawi", "code": "MWK"},
    {"country": "Mexico", "code": "MXN"},
    {"country": "Malaysia", "code": "MYR"},
    {"country": "Mozambique", "code": "MZN"},
    {"country": "Namibia", "code": "NAD"},
    {"country": "Nigeria", "code": "NGN"},
    {"country": "Nicaragua", "code": "NIO"},
    {"country": "Norway", "code": "NOK"},
    {"country": "Nepal", "code": "NPR"},
    {"country": "New Zealand", "code": "NZD"},
    {"country": "Oman", "code": "OMR"},
    {"country": "Panama", "code": "PAB"},
    {"country": "Peru", "code": "PEN"},
    {"country": "Papua New Guinea", "code": "PGK"},
    {"country": "Philippines", "code": "PHP"},
    {"country": "Pakistan", "code": "PKR"},
    {"country": "Poland", "code": "PLN"},
    {"country": "Paraguay", "code": "PYG"},
    {"country": "Qatar", "code": "QAR"},
    {"country": "Romania", "code": "RON"},
    {"country": "Serbia", "code": "RSD"},
    {"country": "Russia", "code": "RUB"},
    {"country": "Rwanda", "code": "RWF"},
    {"country": "Saudi Arabia", "code": "SAR"},
    {"country": "Solomon Islands", "code": "SBD"},
    {"country": "Seychelles", "code": "SCR"},
    {"country": "Sudan", "code": "SDG"},
    {"country": "Sweden", "code": "SEK"},
    {"country": "Singapore", "code": "SGD"},
    {"country": "Saint Helena", "code": "SHP"},
    {"country": "Sierra Leone", "code": "SLE"},
    {"country": "Somalia", "code": "SOS"},
    {"country": "Suriname", "code": "SRD"},
    {"country": "South Sudan", "code": "SSP"},
    {"country": "São Tomé and Príncipe", "code": "STN"},
    {"country": "Syria", "code": "SYP"},
    {"country": "Eswatini", "code": "SZL"},
    {"country": "Thailand", "code": "THB"},
    {"country": "Tajikistan", "code": "TJS"},
    {"country": "Turkmenistan", "code": "TMT"},
    {"country": "Tunisia", "code": "TND"},
    {"country": "Tonga", "code": "TOP"},
    {"country": "Turkey", "code": "TRY"},
    {"country": "Trinidad and Tobago", "code": "TTD"},
    {"country": "Tuvalu", "code": "TVD"},
    {"country": "Taiwan", "code": "TWD"},
    {"country": "Tanzania", "code": "TZS"},
    {"country": "Ukraine", "code": "UAH"},
    {"country": "Uganda", "code": "UGX"},
    {"country": "United States", "code": "USD"},
    {"country": "Uruguay", "code": "UYU"},
    {"country": "Uzbekistan", "code": "UZS"},
    {"country": "Venezuela", "code": "VES"},
    {"country": "Vietnam", "code": "VND"},
    {"country": "Vanuatu", "code": "VUV"},
    {"country": "Samoa", "code": "WST"},
    {"country": "CEMAC", "code": "XAF"},
    {"country": "Organisation of Eastern Caribbean States", "code": "XCD"},
    {"country": "International Monetary Fund", "code": "XDR"},
    {"country": "CFA", "code": "XOF"},
    {"country": "Collectivités d'Outre-Mer", "code": "XPF"},
    {"country": "Yemen", "code": "YER"},
    {"country": "South Africa", "code": "ZAR"},
    {"country": "Zambia", "code": "ZMW"},
    {"country": "Zimbabwe", "code": "ZWL"},
    {"country": "Austria", "code": "EUR"},
    {"country": "Belgium", "code": "EUR"},
    {"country": "Cyprus", "code": "EUR"},
    {"country": "Estonia", "code": "EUR"},
    {"country": "Finland", "code": "EUR"},
    {"country": "France", "code": "EUR"},
    {"country": "Germany", "code": "EUR"},
    {"country": "Greece", "code": "EUR"},
    {"country": "Ireland", "code": "EUR"},
    {"country": "Italy", "code": "EUR"},
    {"country": "Latvia", "code": "EUR"},
    {"country": "Lithuania", "code": "EUR"},
    {"country": "Luxembourg", "code": "EUR"},
    {"country": "Malta", "code": "EUR"},
    {"country": "Netherlands", "code": "EUR"},
    {"country": "Portugal", "code": "EUR"},
    {"country": "Slovakia", "code": "EUR"},
    {"country": "Slovenia", "code": "EUR"},
    {"country": "Spain", "code": "EUR"},
    {"country": "Andorra", "code": "EUR"},
    {"country": "Kosovo", "code": "EUR"},
    {"country": "Monaco", "code": "EUR"},
    {"country": "Montenegro", "code": "EUR"},
    {"country": "San Marino", "code": "EUR"},
    {"country": "Vatican City", "code": "EUR"},
    {"country": "Akrotiri and Dhekelia", "code": "EUR"},
    {"country": "Clipperton Island", "code": "EUR"},
    {"country": "French Southern and Antarctic Lands", "code": "EUR"},
    {"country": "Saint Barthélemy", "code": "EUR"},
    {"country": "Saint Martin", "code": "EUR"},
    {"country": "Saint Pierre and Miquelon", "code": "EUR"},
    {"country": "Eurozone", "code": "EUR"}
]

def get_currency_code(currency, type):

    if type.lower() == 'code':
        if currency in codes:
            return currency
    elif type.lower() == 'currency':
        for x in currency_names:
            if currency.title() == x["currency"]:
                return x["code"]
    elif type.lower() == 'country':
        for y in country_names:
            if currency.title() == y["country"]:
                return y["code"]
            
    return None

def get_currency_code2(currency):

    if currency.upper() in codes:
            return currency
    for x in currency_names:
            if currency.title() == x["currency"]:
                return x["code"]
    for y in country_names:
            if currency.title() == y["country"]:
                return y["code"]
            
    return None

def get_result(from_currency, to_currency, amount):
    # Define the base URL for the API
    base_url = "https://v6.exchangerate-api.com/v6/dcdb738c6f37d5effa0cda91/pair/"

    # Send a GET request to the API and get the response
    response = requests.get(base_url + from_currency + "/" + to_currency + "/" + str(amount))

    # Convert the response to JSON
    data = response.json()

    # Get the exchange rate from the JSON data
    exchange_rate = data.get("conversion_rate")
    converted_amount = data.get("conversion_result")

    # Print the exchange rate and the converted amount
    print(f"Exchange rate: 1 {from_currency} = {exchange_rate} {to_currency}")
    print(f"Converted amount: {converted_amount} {to_currency}")

    # Return
    return

def convert_currency():
    # Ask the user for the currencies and the amount
    #from_currency_type = input("Do you want to enter the first currency as currency code, currency name or country name? (please type code, currency or country): ")
    from_currency = input("Enter the currency to convert from (as currency code, currency name or country name): ")
    from_currency = get_currency_code2(from_currency)
    if from_currency == None:
        again = input("The currency provided doesn't exist. Do you want to try again? (yes or no): ")
        if again.lower() == "yes":
            convert_currency()
        else:
             return
    
    #to_currency_type = input("Do you want to enter the second currency as currency code, currency name or country name? (please type code, currency or country): ")
    to_currency = input("Enter the currency to convert to (as currency code, currency name or country name): ")
    to_currency = get_currency_code2(to_currency)
    if to_currency == None:
        again = input("The currency provided doesn't exist. Do you want to try again? (yes or no): ")
        if again.lower() == "yes":
            convert_currency()
    
    amount = float(input("Enter the amount: "))

    # Get the exchange rate
    get_result(from_currency, to_currency, amount)

    # Ask the user if they want to convert a new amount
    again = input("Do you want to convert a new amount? (yes/no): ")
    if again.lower() == "yes":
        convert_currency()

# Call the function to start the currency conversion
convert_currency()
