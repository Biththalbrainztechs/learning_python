"""
Exercise 2: Event-Driven Programming
Learning the pattern used by LiveKit for handling events

"""
import asyncio
from typing import Callable, List, Dict, Any
from datetime import datetime
import inspect


class EventEmitter:
    """
    Simple event system similar to Node.js EventEmitter . 
    This is the pattern LiveKit uses for handling room events

    """

    def __init__(self):
        self.listeners:Dict[str,list[Callable]]={}
    
        '''
        listeners is a dictionary
        where keys are strings (event names)
        and values are lists of functions (handlers).
        '''


    def on(self,event_name:str,callback:Callable):
      
        """
        Register an event listener
        Example : 
        emitter.on('user_joined',handle_user_joined)

        """
        if event_name not in self.listeners:
            self.listeners[event_name]=[]
        self.listeners[event_name].append(callback)
        print(f"Registered listener for'{event_name}'")
    
    async def emit(self,event_name:str,data:Any=None):
        """
        Register an event listener 

        Example : 
        
            await emitter.emit ('user_joined',{'name':'Alice'})
        
        """
        print(f"Event'{event_name} triggered")

        if event_name not in self.listeners:
            print(f"No listeners registered for {event_name}")
            return
    
        for callback in self.listeners[event_name]:
            if inspect.iscoroutinefunction(callback):
                await callback(data)
            else:
                callback(data)


async def on_user_joined(data:dict):
    """ Handle when a user joinss"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp} user joined: {data['name']}]")

    await asyncio.sleep(0.5)
    print(f"[{timestamp}] saved user {data['name']} to database]")

async def on_user_left(data:dict):
    """ Handle when a user leaves """
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] User left :{data['name']}")

def on_message(data:dict):
    """ Handle chat message (non-asyn example)"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {data['sender']}:{data['message']}" )

def on_wave_hi(data:dict):
    """ Handle video hi"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {data['user']} {data['action']}" )


async def on_audio_track(data:dict):
    """ Handle audio track events"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    action = "started" if data['enabled'] else "stopped"
    print(f"[{timestamp}] {data['user']} {action} speaking")

async def on_video_track(data:dict):
    """ Handles video tracks"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    action = "turned on" if data['enabled']else "turned of"
    print(f"[{timestamp}] {data['user']} {action} video")


async def main():
    print("=" * 60)
    print("EVENT-DRIVEN PROGRAMMING DEMO")
    print("=" * 60)

    emitter = EventEmitter()

    print("\n Registering Event handlers....")
    emitter.on('user_joined',on_user_joined)
    emitter.on('user_left',on_user_left)
    emitter.on('message',on_message)
    emitter.on('audio_track',on_audio_track)
    emitter.on('video_track',on_video_track)
    emitter.on('on_wave_hi',on_wave_hi)

    print('\n 2 Simulating Room Events .......')

    await emitter.emit('user_joined',{'name':'Alice','id':'001'})
    await emitter.emit('user_joined',{'name':'Bob','id':'002'})

    await emitter.emit('message',{
        'sender':'Alice',
        'message':'Hey everyone!'
    })
    await emitter.emit ('video_track',{
        'user':"Alice",
        'enabled':True
    })

    await emitter.emit('on_wave_hi',{
        'user':'Alice',
        'action':'waved hi!'
    })
   

    await emitter.emit('audio_track',{
        'user':'Alice',
        'enabled': True
    })

    await emitter.emit('message',{
        'sender':'Bob',
        'message':"Hi Alice!!"
    })

    await emitter.emit('audio_track',{
        'user':"Alice",
        "enabled":False

    })


    await emitter.emit("user_left",{'name':'Bob','id':'002'})

    


    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)
    print("\n Key Concepts:")
    print("   - Events decouple code (emit doesn't need to know about handlers)")
    print("   - Multiple handlers can listen to the same event")
    print("   - Async handlers allow non-blocking event processing")
    print("   - This is how LiveKit notifies you about room events!")

if __name__ == "__main__":
    asyncio.run(main())
