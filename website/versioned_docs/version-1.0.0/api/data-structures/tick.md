---
sidebar_position: 1
---

# Tick

## Tick
This is a structure for storing the latest prices of the symbol. It is designed for fast retrieval of the most requested information about current prices.

### Example
```
class MyEA(ExpertAdvisor):
    ...
    def on_tick(self, tick):
        print(tick.time)        # 2022-04-13
        print(tick.bid)         # 100.32
        print(tick.ask)         # 100.31
        print(tick.last)        # 100.33
        print(tick.volume)      # 10000
        print(tick.time_msc)    # 10
        print(tick.flags)       # 0
        print(tick.volume_real) # 10000
        
```

### Props
|  Name       |  Type             |  Description   |
| ----        | ----            |  ----           |
| time        | datetime             |  Time of the last prices update    |
| bid        | float             |  Current Bid price    |
| ask        | float             |  Current Ask price    |
| last        | int            |  Price of the last deal (Last)    |
| volume        | int            |  Volume for the current Last price    |
| time_msc        | int            |  Time of a price last update in milliseconds    |
| flags        | int            |  Tick flags    |
| volume_real        | float             |  Volume for the current Last price with greater accuracy    |

