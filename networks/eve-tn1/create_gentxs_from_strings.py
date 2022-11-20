import json, os

# get current_dir
current_dir = os.path.dirname(os.path.realpath(__file__))

FOLDER_NAME="gentx"
GENTXS = [
    # pbcups
    '''{"body":{"messages":[{"@type":"/cosmos.staking.v1beta1.MsgCreateValidator","description":{"moniker":"pbcups_testnet","identity":"","website":"https://reece.sh","security_contact":"reece@reece.sh","details":""},"commission":{"rate":"0.050000000000000000","max_rate":"0.200000000000000000","max_change_rate":"0.050000000000000000"},"min_self_delegation":"1","delegator_address":"eve1hj5fveer5cjtn4wd6wstzugjfdxzl0xpysfwwn","validator_address":"evevaloper1hj5fveer5cjtn4wd6wstzugjfdxzl0xp9c4605","pubkey":{"@type":"/cosmos.crypto.ed25519.PubKey","key":"eOVVqQBnfoH2QCF6Ia+whevWCnUOQzE+YdYEiRCFcTc="},"value":{"denom":"ujoe","amount":"1000000"}}],"memo":"33e3f7d7ff069ac968ef30f300deb2eff9bac626@95.217.113.126:26656","timeout_height":"0","extension_options":[],"non_critical_extension_options":[]},"auth_info":{"signer_infos":[{"public_key":{"@type":"/cosmos.crypto.secp256k1.PubKey","key":"ApZa31BR3NWLylRT6Qi5+f+zXtj2OpqtC76vgkUGLyww"},"mode_info":{"single":{"mode":"SIGN_MODE_DIRECT"}},"sequence":"0"}],"fee":{"amount":[],"gas_limit":"200000","payer":"","granter":""},"tip":null},"signatures":["pYrl5+5THcmkntBYo3JpPlBP9UgwY4UMXqBlpoy9g4hFmjfhtGr0siuCbcmGDJ3wPG/9yS5lpqopzfZl0QSJBA=="]}''',    
]

os.makedirs(FOLDER_NAME, exist_ok=True)

for gentx in GENTXS:
    v = json.loads(gentx)
    moniker = v['body']['messages'][0]['description']['moniker']
    memo = v['body']['memo']
    if '@' in memo: print(f"{moniker} - {memo}")

    # create file named moniker.json    
    with open(f"{os.path.join(current_dir, FOLDER_NAME, moniker)}.json", "w") as f:        
        json.dump(v, f)        

print(f"ALL GENTXS CREATED FROM STRINGS. Run add-genesis-accounts.py")