import json
f='/home/akash/jsonfile.json'
with open(f, 'r') as file:
	d=json.loads(file.read())
print(d["Records"][0]["s3"]["bucket"]["arn"])
