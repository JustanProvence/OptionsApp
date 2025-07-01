from polygon import RESTClient

client = RESTClient()

options_chain = []
for o in client.list_snapshot_options_chain(
    "CLSK",
    params={
        "strike_price": 11,
        "contract_type": "call",
        "order": "asc",
        "limit": 5,
        "sort": "expiration_date",
    },
):
    options_chain.append(o)

print(options_chain[0])