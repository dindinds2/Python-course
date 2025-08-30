class employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Employee delate")

def create_obj():
    print("Making object")
    obj = employee()
    print("End of fucntion")
    return obj

print("Calling create_obj fucntion")
obj = create_obj()
print("End of program")
