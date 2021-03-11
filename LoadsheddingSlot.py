from datetime import datetime
from pytz import timezone

class LoadsheddingSlot:
  def __init__(self, start, end):
    self.start = datetime.strptime(start, "%H:%M").time()
    self.end = datetime.strptime(end, "%H:%M").time()
    
  def isSlotActive(self):
    now = datetime.now(timezone("Africa/Johannesburg")).time()
    return self.start <= now and now <= self.end
