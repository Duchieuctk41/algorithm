class Elsys():
    def __init__(self, data, fport=0):
        self.result = self.decrypt(data)
        self.name = 'cc'
    
    def bin16dec(self,bin):
            num = bin & 0xFFFF
            if (0x8000 & num):
                num = -(0x010000 - num)
            return num 
        
    def bin8dec(self, bin):
        num = bin & 0xFF
        if (0x80 & num):
            num = -(0x0100 - num)
        return num

    def decrypt(self, byteString) :
        byteArray = bytearray.fromhex(byteString)
        rangeByte = len(byteArray)
        skip = 0
        result = {}
        for i in range (rangeByte):
            if skip > 0 :
                skip = skip -1
                continue
            #Temperature -3276.8°C -->3276.7°C
            if byteArray[i].to_bytes(1,'big') == b'\x01':  
                temperature = (byteArray[i+1] << 8 | byteArray[i+2])
                temperature = self.bin16dec(temperature)
                result['temperature'] = temperature/10
                skip = 2

            #Humidity 0-100%
            elif byteArray[i].to_bytes(1,'big') == b'\x02':
                result['humidity'] = byteArray[i+1]
                skip = 1

            #Acceleration -128 --> 127 +/-63=1G
            elif byteArray[i].to_bytes(1,'big') == b'\x03':
                result["x"] = self.bin8dec(byteArray[i+1])
                result["y"] = self.bin8dec(byteArray[i+2])
                result["z"] = self.bin8dec(byteArray[i+3])
                skip = 3

            #Light 0-->65535 Lux
            elif byteArray[i].to_bytes(1,'big') == b'\x04':
                result["light"] = (byteArray[i+1] << 8 | byteArray[i+2])
                skip = 2

            #Motion sensor (PIR)
            elif byteArray[i].to_bytes(1,'big') == b'\x05':
                result['motion'] =  byteArray[i+1]
                skip = 1

            #CO2 0-65535 ppm
            elif byteArray[i].to_bytes(1,'big') == b'\x06':
                co2 = (byteArray[i+1] << 8 | byteArray[i+2])
                result['co2'] = co2
                skip = 2

            #Battery 0-65535mV
            elif byteArray[i].to_bytes(1,'big') == b'\x07':
                vdd = (byteArray[i+1] << 8 | byteArray[i+2])
                result['vdd'] = vdd
                skip = 2

            #Analog input 10-65535mV
            elif byteArray[i].to_bytes(1,'big') == b'\x08':
                vdd = (byteArray[i+1] << 8 | byteArray[i+2])
                result['analog1'] = vdd
                skip = 2

            #GPS lat long 
            elif byteArray[i].to_bytes(1,'big') == b'\x09':
                if (byteArray[i + 2] & 0x80):
                    byteParsedLat  = 0xFF << 24
                else:
                    byteParsedLat = 0
                if (byteArray[i + 5] & 0x80):
                    byteParsedLng  = 0xFF << 24
                else:
                    byteParsedLng = 0

                result['lat'] = (byteArray[i + 0] | byteArray[i + 1] << 8 | byteArray[i + 2] << 16 | byteParsedLat) / 10000
                result['long'] = (byteArray[i + 3] | byteArray[i + 4] << 8 | byteArray[i + 5] << 16 | byteParsedLng) / 10000
                skip = 5

            #relative pulse count
            elif byteArray[i].to_bytes(1,'big') == b'\x0A':
                pulse1 = (byteArray[i+1] << 8 | byteArray[i+2])
                result['pulse1'] = pulse1
                skip = 2
                continue

            #PULSE1_ABS 0->0xFFFFFFFF
            elif byteArray[i].to_bytes(1,'big') == b'\x0B':
                pulseAbs = (byteArray[i + 1] << 24) | (byteArray[i + 2] << 16) | (byteArray[i + 3] << 8) | (byteArray[i + 4])
                result['pulseAbs'] = pulseAbs
                skip = 4
                continue
            
            #EXT_TEMP1 -3276.5C-->3276.5C
            elif byteArray[i].to_bytes(1,'big') == b'\x0C':
                temp = (byteArray[i + 1] << 8) | (byteArray[i + 2])
                temp = self.bin16dec(temp) / 10
                result["externalTemperature"] = temp
                skip = 2
                continue

            #EXT_DIGITAL value 1 or 0
            elif byteArray[i].to_bytes(1,'big') == b'\x0D':
                digital = (byteArray[i + 1])
                result["digital"] = digital
                skip = 1
                continue

            # distance in mm
            elif byteArray[i].to_bytes(1,'big') == b'\x0E':
                distance = (byteArray[i+1] << 8 | byteArray[i+2])
                result['distance'] = distance
                skip = 2

            #number of vibration/motion
            elif byteArray[i].to_bytes(1,'big') == b'\x0F':
                accMotion = byteArray[i+1]
                result["accMotion"] = accMotion
                skip = 1
                continue
            
            #internal temp 2bytes external temp -3276.5C-->3276.5C
            elif byteArray[i].to_bytes(1,'big') == b'\x10':
                iTemp = (byteArray[i + 1] << 8) | (byteArray[i + 2])
                iTemp = self.bin16dec(iTemp)
                eTemp = (byteArray[i + 3] << 8) | (byteArray[i + 4])
                eTemp = self.bin16dec(eTemp)
                result["irInternalTemperature"] = iTemp / 10
                result["irExternalTemperature"] = eTemp / 10
                skip = 4
                continue

            #Body occupancy
            elif byteArray[i].to_bytes(1,'big') == b'\x11':
                result['occupancy'] =  byteArray[i+1]
                skip = 1
                continue

            #WATERLEAK 0-255
            elif byteArray[i].to_bytes(1,'big') == b'\x12':
                result['waterleak'] =  byteArray[i+1]
                skip = 1
                continue

            #temperature data 1byte ref+64byte external temp
            elif byteArray[i].to_bytes(1,'big') == b'\x13':
                ref = byteArray[i+1]
                i = i+1 
                grideye = []
                for j in range (64):
                    grideye.append(ref + (byteArray[1+i+j]/10))
                skip = 64
                continue

            #extenal pressure data (hPa)
            elif byteArray[i].to_bytes(1,'big') == b'\x14':
                pressure = (byteArray[i + 1] << 24) | (byteArray[i + 2] << 16) | (byteArray[i + 3] << 8) | (byteArray[i + 4])
                result["pressure"] = pressure / 1000
                skip = 4
                continue

            #sound data (peak/avg)
            elif byteArray[i].to_bytes(1,'big') == b'\x15':
                result['soundPeak'] = byteArray[i+1]
                result['soundAvg'] = byteArray[i+2]
                skip = 2
                continue 

            #PULSE 2 0-->0xFFFF
            elif byteArray[i].to_bytes(1,'big') == b'\x16':
                pulse2 = (byteArray[i + 1] << 8) | (byteArray[i + 2])
                result["pulse2"] = pulse2
                skip = 2
                continue

            #PULSE2_ABS  no 0->0xFFFFFFFF
            elif byteArray[i].to_bytes(1,'big') == b'\x17':
                pulseAbs2 = (byteArray[i + 1] << 24) | (byteArray[i + 2] << 16) | (byteArray[i + 3] << 8) | (byteArray[i + 4])
                result["pulseAbs2"] = pulseAbs2
                skip = 4
                continue

            #ANALOG2 voltage in mV
            elif byteArray[i].to_bytes(1,'big') == b'\x18':
                analog2 = (byteArray[i + 1] << 8) | (byteArray[i + 2])
                result["analog2"] = analog2
                continue

            #EXT_TEMP2 -3276.5C-->3276.5C
            elif byteArray[i].to_bytes(1,'big') == b'\x19':
                temp = (byteArray[i + 1] << 8) | (byteArray[i + 2])
                temp = self.bin16dec(temp)
                result["externalTemperature2"] = temp / 10
                skip = 2
                continue

            #EXT_DIGITAL2 value 1 or 0
            elif byteArray[i].to_bytes(1,'big') == b'\x1A':
                digital2 = byteArray[i + 1]
                result["digital2"] = digital2
                skip = 1
                continue

            #EXT_ANALOG_UV  signed int (uV)
            elif byteArray[i].to_bytes(1,'big') == b'\x1B':
                analogUv = (byteArray[i + 1] << 24) | (byteArray[i + 2] << 16) | (byteArray[i + 3] << 8) | (byteArray[i + 4])
                skip = 4
                continue

            #TVOC (ppb)
            elif byteArray[i].to_bytes(1,'big') == b'\x1C':
                tvoc = (byteArray[i + 1] << 8) | (byteArray[i + 2])
                skip = 2
                continue

            #debug
            elif byteArray[i].to_bytes(1,'big') == b'\x3D':
                continue
        return result
    
    def printDecrypt(a):
        print(a.result)

p1 = Elsys('0100dc02340601fc070e2f',0)
p1.printDecrypt()