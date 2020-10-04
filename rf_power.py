#!/usr/bin/python3

import asyncio

latitude = 0
longitude = 0
altitude = 0

async def gps_reader(ip, port):
    reader, writer = await asyncio.open_connection(ip, port)  
    while True:
        print ('Reading\n')
        data = await reader.readline()
        print ('Readed data: ' + str(data)) # Update globarl vars / sync

async def power_reader ():
    proc = await asyncio.create_subprocess_exec(
        'rtl_power', '-p', '1', '-i', '5', '-f', '432100k:432112k:12k',
        stdout=asyncio.subprocess.PIPE)
    try:
        while True:
            data = await proc.stdout.readline()
            line = data.decode('ascii').rstrip()
            data = line.split(', ')
            print (str(data))
            
    except:
        print("Unexpected error:", sys.exc_info()[0])
        proc.kill()
        raise

async def main ():
    await asyncio.gather(power_reader(), gps_reader("192.168.1.16", 11123))
    
if __name__ == "__main__":
    asyncio.run (main())
