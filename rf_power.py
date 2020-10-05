#!/usr/bin/python3

import asyncio
import sys

latitude = 0
longitude = 0
altitude = 0
fix_quality = 0
lock = asyncio.Lock()

async def connect_gps(ip, port):
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, port)
            return reader
        except:
            print("Cannot Connect, waiting...")
            await asyncio.sleep(1)

async def gps_reader(ip, port):
    reader = await connect_gps(ip, port)
    
    while True:
        global altitude, latitude, longitude, fix_quality, lock
        try:
            data = await reader.readline()
            data = data.decode().split(',')
            async with lock:
                altitude = data[9]
                latitude = data[2]
                longitude = data[4]
                fix_quality = data[6]
        except:
            altitude = latitude = longitude = fix_quality = 0
            reader = await connect_gps(ip, port)
            continue
        
async def power_reader ():
    proc = await asyncio.create_subprocess_exec(
        'rtl_power', '-p', '1', '-i', '1', '-f', '432100k:432112k:12k',
        stdout=asyncio.subprocess.PIPE)
    try:
        while True:
            global lock
            data = await proc.stdout.readline()
            line = data.decode('ascii').rstrip()
            data = line.split(', ')
            async with lock:
                data.append(latitude)
                data.append(longitude)
                data.append(altitude)
                data.append(fix_quality)
            print (str(data))
            
    except:
        print("Unexpected error:", sys.exc_info()[0])
        proc.kill()
        raise

async def main ():
    await asyncio.gather(power_reader(), gps_reader("192.168.1.4", 11123))
    
if __name__ == "__main__":
    asyncio.run (main())
