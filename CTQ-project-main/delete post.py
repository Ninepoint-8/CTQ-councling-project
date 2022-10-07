from supabase import create_client, Client

url: str = "https://zvxlqpfkfudfdqedqoyu.supabase.co"
# key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp2eGxxcGZrZnVkZmRxZWRxb3l1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjE5NTY2OTgsImV4cCI6MTk3NzUzMjY5OH0.1MfObcGD01cJhUEJC6sowQ71xWyXD__HNmDcM5ALwig"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp2eGxxcGZrZnVkZmRxZWRxb3l1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2MTk1NjY5OCwiZXhwIjoxOTc3NTMyNjk4fQ.Z6THxR-f68TDk0uAdPrZmp93iQ00-PV5yRjkk1DOe_M"
supabase: Client = create_client(url, key)
data = supabase.table("posts").delete().eq("id", 2).execute()
print(data)