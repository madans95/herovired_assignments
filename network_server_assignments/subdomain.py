import requests, time
from tabulate import tabulate

def check_subdomain_status(list_of_subdomains):
    results = []
    for sub_domain in list_of_subdomains:
        try:
            response = requests.get(f"http://{sub_domain}", timeout=1)
            if response.status_code == 200:
                status = "Up" 
            else:
                status = "Down"
        except requests.ConnectionError:
            status = "Down"
        except requests.Timeout:
            status = "Timeout"
        except Exception as e:
            status = str(e)
        
        results.append([sub_domain, status])
    
    return results

def display_table(data):
    headers = ["Subdomain", "Status"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    list_of_subdomains = ["aws.amazon.com", "gaming.amazon.com", "music.amazon.com","smile.amazon.com"]

    while True:
        results = check_subdomain_status(list_of_subdomains)
        display_table(results)
        time.sleep(60)