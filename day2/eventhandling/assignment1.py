import asyncio
from typing import Callable,List,Dict,Any
from datetime import datetime
import inspect

class EventEmitter:

    def __init__(self):
        self.listerners:Dict[str,list[Callable]]={}

    def on(self,event_name:str,callback:Callable):
        
        if event_name not in self.listerners:
            self.listerners["event_name"].append(callback)
            print(f"Registered listener for '{event_name}")
    
    async def emit(self,event_name:str,data:Any = None):
        """ Triggers an Event """
        if event_name not in self.listerners:
            return
        
        for callback in self.listerners['event_name']:
            if inspect.iscoroutinefunction(callback):
                await callback(data)
            else:
                callback(data)
        
    def off(self,event_name:str,callback:Callable):
        if event_name in self.listerners:
            del self.listerners['event_name']
            print(f'{event_name} is removed')
        else :
            return
        
async def on_user_joined(data:dict):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}]: Welcome {data["user_name"]}. It's good to see you")
    await asyncio.sleep(0.5)
    print(f"[{timestamp}] saved user {data['name']} to database")

async def on_user_left(data:dict):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}]: {data["user_name"]}. See you soon")
    await asyncio.sleep(0.2)
    
async def on_message_sent(data:dict):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}]: {data["sender"]}:{data['content']}")
    await asyncio.sleep(0.1)
    print(f"{data["message_id"]} is stored in database")

async def on_message_edited(data:dict):
    print(f"{data["old_content"]}\n")
    print(f"{data["message_id"]} from {data["sender"]} is edited\n")
    await asyncio.sleep(0.1)
    print(f"{data["message_id"]} is stored in database")
    print(f"(edited)[{data["new_content"]}\n") 

async def on_message_deleted(data:dict):
    print(f"{data["message_id"]} from {data["sender"]} is deleted\n")
    await asyncio.sleep(0.1)
    print(f"{data["message_id"]} is deleted in database")

def on_user_typing(data:dict):
    print(f" {data["username"]} is typing... ")
    print(f"💬💬💬💬")
    

def on_user_stopped_typing(data:dict):
    print(f" {data["username"]} stopped typing... ")

async def on_reaction_added(data:dict):
    print(f"{data["user"]}{data["emoji"]} the message {data["message_id"]} \n")
    await asyncio.sleep(0.1)
    print(f"{data["message_id"]} is updated in database")


