import simple.simple_pb2 as simple_pb2

simple_message = simple_pb2.SimpleMessage()
simple_message.id = 123
simple_message.is_simple = True
simple_message.name = "This is a simple message using Python"

sample_list = simple_message.sample_list
sample_list.append(3)
sample_list.append(4)
sample_list.append(5)

#print(simple_message)
#print(sample_list)

with open ("simple.bin", "wb") as f:
    print("Rrite as binary file")
    bytesAsString = simple_message.SerializeToString()
    f.write(bytesAsString)

with open ("simple.bin", "rb") as f:
    print("Read binary file")
    simple_message_read = simple_pb2.SimpleMessage().FromString(f.read())

print(simple_message_read)
#print("Is Simple?: " + simple_message_read.is_simple)
print("Is Simple?: " + str(simple_message.is_simple))
print("Id?: " + str(simple_message.id))
