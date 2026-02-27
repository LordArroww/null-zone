import urllib.request
import json
import ssl

try:
    url = "https://null-zone-backend.santiferreri14.workers.dev"
    data = json.dumps({"code": "TESTER-ZERO"}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    res = urllib.request.urlopen(req, timeout=5)
    print("SUCCESS", res.getcode())
except Exception as e:
    import traceback
    traceback.print_exc()
