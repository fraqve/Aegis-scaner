import json
import requests


def load_config(config_file:str):
    with open(config_file) as file:
        config = json.load(file)
    return config



def check_virustotal(ip:str,api:str):
    data = {
        "malicious": 0,
        "suspicious": 0,
        "harmless": 0,
        "undetected": 0,
        "error": None
    }

    try:
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

        headers = {
            "accept": "application/json",
            "x-apikey":api
        }


        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            raw_stats = response.json()
            target_stats = raw_stats["data"]["attributes"]["last_analysis_stats"]

            for key in target_stats:
                if key != "timeout":
                    data[key] = target_stats[key]
            return data
        

        else:
            data["error"] = f"Error:{response.status_code}"
            return data


    except requests.ConnectionError:
        data["error"] = "Error: No internet connexion"
        return data

    except Exception as e:
        data["error"] = f"An error has occured: {e}"
        return data





def check_abuseipdb(ip:str,api:str):
    data = {
        "abuseConfidenceScore": 0,
        "error": None
    }

    try:
        url = f"https://api.abuseipdb.com/api/v2/check"
        query_params = {
            "ipAddress":ip,
            "maxAgeInDays": "90"
        }

        query_headers = {
            'Accept': 'application/json',
            'Key': api
        }

        response = requests.get(url,headers=query_headers,params=query_params)

        if response.status_code == 200:
            raw_data = response.json()
            data["abuseConfidenceScore"] = raw_data["data"]["abuseConfidenceScore"]
            return data
        
        else:
            data["error"] = f"Error:{response.status_code}"
            return data

    except requests.ConnectionError:
        data["error"] = "Error: no internet connexion"
        return data

    except Exception as e:
        data["error"] = f"An error has occured: {e}"
        return data


