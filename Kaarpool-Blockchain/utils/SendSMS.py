import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {
    "authorization": "AR2dqJ9iCS0Lux7kTwG1ZDa8UXeIVv3M5tOcpsQnFhmbofjzy6MDNf6FbB8sWzOCdQmG9u0VIeqTJ5Uc",
    "message": "This is test Message sent from \
		Python Script using REST API.",
    "language": "english",
    "route": "q",
    "numbers": "9970533440"}

headers = {
    'cache-control': "no-cache"
}
try:
    response = requests.request("GET", url,
                                headers=headers,
                                params=querystring)
    print(response)

    print("SMS Successfully Sent")
except:
    print("Oops! Something wrong")

# curl -X POST \
#   https://www.fast2sms.com/dev/bulkV2 \
#   -H 'authorization: YOUR_API_KEY' \
#   -d 'message=This is a test message&language=english&route=q&numbers=9999999999,8888888888,7777777777'

# curl -x GET \
#   'https://www.fast2sms.com/dev/bulkV2?authorization=YOUR_API_KEY&sender_id=TXTIND&message=This is a test message&route=v3&numbers=9999999999,8888888888,7777777777'
