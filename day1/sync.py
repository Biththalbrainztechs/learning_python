import time 
# synchronous (blocking example)
def make_coffee():
    print("starting cofeee.....")
    time.sleep(3)
    print("coffeee readyyy")
    return "="

def make_toast():
    print("starting toast....")
    time.sleep(2)
    print("Toast ready")
    return "🍞"

coffee = make_coffee()
toast = make_toast()

print(f"BreakFast:{coffee}{toast}")

#total second to make coffee and toast was 3 + 2 seconds 

