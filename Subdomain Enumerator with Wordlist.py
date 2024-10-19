import requests

def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"✅ Found: {url}")
    except requests.ConnectionError:
        pass

def enumerate_subdomains(domain, wordlist):
    with open(wordlist, 'r') as file:
        subdomains = file.read().splitlines()

    print(f"🌍 Enumerating subdomains for {domain}...")
    for subdomain in subdomains:
        check_subdomain(domain, subdomain)

if __name__ == "__main__":
    target_domain = input("🔗 Enter target domain: ")
    wordlist_file = input("📜 Enter path to subdomain wordlist: ")
    enumerate_subdomains(target_domain, wordlist_file)
