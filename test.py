import nft_storage

# Replace with your NFT.Storage API key
API_KEY = "456417ec.101b3a079815487ba477d21c7d2c20e8"

# Path to your image file
image_path = "test.png"  # Replace with your actual path

# Initialize NFTStorage client
client = nft_storage.ApiClient(nft_storage.Configuration(api_key=API_KEY))

# Open the image file in binary mode
with open(image_path, "rb") as f:
    # Upload the image
    data = f.read()
    response = client

# Get the IPFS CID (content identifier) and IPFS URL
ipfs_cid = response["cid"]
ipfs_url = f"https://ipfs.io/ipfs/{ipfs_cid}"

print(f"Image uploaded to IPFS! CID: {ipfs_cid}")
print(f"IPFS URL: {ipfs_url}")