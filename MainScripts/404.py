import aiohttp
import asyncio
from aiohttp import ClientSession



async def main():

    with open("C:/Users/Asif/Desktop/all.csv", 'r') as f:
        lines = f.readlines()
        f = ''.join(f)
        f = f.replace('[', '  ')


    for i in range(1766,len(lines)):
        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.get(lines[i]) as response:

                #print("Status:", response.status)

                html = await response.text()
                #print("Body:", html[:15], "...")
                if response.status == 200:
                    with open('E:\\connect\\\404.csv', "a") as myfile:
                        myfile.write(lines[i])
                        print("Done="+(str(i)))


                elif response.status == 404:
                    print("404")






loop = asyncio.get_event_loop()
loop.run_until_complete(main())





