import complex.complex_pb2 as compliex_pb2

complex_message = compliex_pb2.ComplexMessage()

########################################################
# INCORRECT - will not work
########################################################
# one_dummy_message       = compliex_pb2.DummyMessage()
# one_dummy_message.id    = 123
# one_dummy_message.name  = "I am a dummy message"
# complex_message.one_dummy = one_dummy_message
########################################################

complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "I am a one dummy message"

# 1st multiple dummy message
first_multiple_dummy = complex_message.multiple_dummy.add()
first_multiple_dummy.id = 345
first_multiple_dummy.name = "I am the 1st of the multiple dummy messages"

# 2nd multiple dummy message
first_multiple_dummy = complex_message.multiple_dummy.add(id = 567, name = "I am the 2nd of the multiple dummy messages")

# 3rd multiple dummy message
third_dummy_message       = compliex_pb2.DummyMessage()
third_dummy_message.id    = 567
third_dummy_message.name  = "I am the 3rd of the multiple dummy messages"
###################################################################################
# IMPORTANT
# Parameter passed to the 'extend' method below is 'passed by value' (it's a copy)
complex_message.multiple_dummy.extend( [third_dummy_message])
###################################################################################
# This change won't appear in the 3rd dummy message of complex message
# because the call to 'extend' above passed-in third_dummy_message by value (copy)
third_dummy_message.id = 999
###################################################################################

print (complex_message)

#################################################################################
# Protocol Buffer Python Generated Guide
#################################################################################
# https://developers.google.com/protocol-buffers/docs/reference/python-generated
#################################################################################