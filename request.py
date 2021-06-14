from onepasswordconnectsdk.client import new_client

client = new_client(
    "http://localhost:8080",
    "{Your_1Password_Connect_API_Token}"
)

item_details  = client.get_item("{your_item_id}", "{your_vault_id}")

print(client.get_vaults())
print(item_details)