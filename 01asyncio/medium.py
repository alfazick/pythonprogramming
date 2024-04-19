import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        
async def main(urls):
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

# List of URLs to fetch data from
urls = [
    "http://example.com",
    "http://example.org",
    "http://example.net"
]

res = asyncio.run(main(urls))

print([word[:50] for word in res])
# This script concurrently fetches data from three websites and gathers the results.