# Date: 29-Sep-2025
# import json

# with open('alert.json', 'r') as f:
#     a = json.load(f)
#     print(f'Alert {a["alert_id"]}: {a["severity"].upper()} severity {a["alert_type"]} from {a["source_ip"]}')


import json

with open('threat_intel.json', 'r') as f:
    d = json.load(f)
    iocs = d["indicators"]
    ok_iocs = []
    for ioc in iocs:
        if ioc["confidence"] > 80 and ioc["severity"] == 'high':
            ok_iocs.append(ioc)
    
    for ioc in ok_iocs:
        print(ioc["id"])