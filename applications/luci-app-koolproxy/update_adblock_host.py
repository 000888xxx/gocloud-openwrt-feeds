# 提取广告规则，并且只提取对全域禁止的那种规则

import time
import sys
import requests
import re

rules_url = [
    # EasyList China
    'https://easylist-downloads.adblockplus.org/easylistchina.txt',
    # EasyList + China
    # 'https://easylist-downloads.adblockplus.org/easylistchina+easylist.txt',
]

rule = ''

# contain both domains and ips
domains, ips = set(), set()

for rule_url in rules_url:
    print('loading... ' + rule_url)

    # get rule text
    success = False
    try_times = 0
    r = None
    while try_times < 5 and not success:
        r = requests.get(rule_url)
        if r.status_code != 200:
            time.sleep(1)
            try_times = try_times + 1
        else:
            success = True
            break

    if not success:
        sys.exit('error in request %s\n\treturn code: %d' %
                 (rule_url, r.status_code))

    rule = rule + r.text + '\n'

# parse rule
rule = rule.split('\n')
for row in rule:
    row = row.strip()

    if row.startswith('||') and row.endswith('^'):
        row = row[2:-1]
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', row):
            ips.add(row)
        else:
            domains.add(row)

domains = list(domains)
ips = list(ips)

domains.sort()
ips.sort()

with open("root/usr/share/koolproxy/dnsmasq.adblock", "w") as f:
    for domain in domains:
        f.write("address=/{}/0.0.0.0\n".format(domain))
