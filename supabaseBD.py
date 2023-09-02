import os
from supabase import create_client, Client
from decouple import config

url = config("SUPABASE_URL")
key = config("SUPABASE_KEY")

supabase: Client = create_client(url, key)
query = supabase.table("Recursos").select("*").execute()
response = query.data
print("Dados consultados:")
for row in response:
    print(row)