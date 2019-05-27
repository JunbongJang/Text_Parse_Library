import uuid


uuid_file = open("uuid_file.csv", "w")

for x in range(1000):
    uuid_file.write(str(x) + ',')
    temp_uuid = uuid.uuid4()
    uuid_file.write(str(temp_uuid) + '\n')
    print (temp_uuid)