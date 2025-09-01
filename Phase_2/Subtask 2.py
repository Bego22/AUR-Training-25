from time import time
from rich.console import Console 

console = Console()
def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
    else:
        print(msg)



class BaseMsg:
 
    def __init__(self, data: str):
        self._data = data
    @property
    def style(self):
        return '' # BaseMsg-specific

    @property
    def data(self):
        return self._data

    def __str__(self):
        return self._data # BaseMsg-specific

    def __len__(self):
        return len(self.data)

    def __eq__(self, other):
        if isinstance(other,BaseMsg) :
            return self.data == other.data 
        return False 

    def __add__(self, other):
        if isinstance(other, str):
            new_data = self.data + other
        else :
            new_data = self.data + other.data
        
        return self.__class__(new_data) 


class LogMsg(BaseMsg):
    def __init__(self, data):
        super().__init__(data)
        self._timestamp: int = int(time()) 
    def __str__(self):
        return f"[{self._timestamp}] {self.data}"
    @property
    def style(self): # type: ignore
        return 'black on yellow'
    


class WarnMsg(LogMsg):
    def __init__(self, data):
        super().__init__(data)
        self._timestamp: int = int(time())
    def __str__(self):
        return f"[!WARN][{self._timestamp}] {self.data}"
    @property
    def style(self): # type: ignore
        return 'white on red'
    
    
    

if __name__ == '__main__':

    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log')
    m3 = WarnMsg('Warning')
    send_Msg(m1)
    send_Msg(m2)
    send_Msg(m3) 
