import time
print("Hello this is gen ai")

timestamp=time.strftime('%H:%M:%S')
print(timestamp)

#Decalaring variables that holds the system time 
timestamphour=int(time.strftime('%H'))
timestampminute=time.strftime('%M')
timestampseconds=time.strftime('%S')
print()
print(timestamphour)
print(timestampminute)
print(timestampseconds)

timestamphour=int(time.strftime('%H'))
if(0<=timestamphour<12):
  print("Good morning!! How may i assit you")

elif(12<=timestamphour<18):
  print("Good Afternoon")

elif(18<=timestamphour<21):
  print("Good evening sir")

else:
  print("Its already late sir! time to sleep !!")
  print("ask how amy i assit you sir")