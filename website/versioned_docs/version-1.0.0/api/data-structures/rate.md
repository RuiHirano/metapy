---
sidebar_position: 2
---

# Rate

## Rate
This structure stores information about the prices, volumes and spread.

### Example
```
class MyEA(ExpertAdvisor):
    ...
    def on_tick(self, tick):
        rates = GetNRatesByStartPosition("USDJPY", 0, 0, 100)
        for rate in rates:
            print(rate.time)         # 2022-04-13
            print(rate.open)         # 100.13
            print(rate.high)         # 100.24
            print(rate.low)          # 100.10
            print(rate.close)        # 100.25
            print(rate.tick_volume)  # 10000
            print(rate.spread)       # 3
            print(rate.real_volume)  # 23000
        
```

### Props
|  Name       |  Type             |  Description   |
| ----        | ----            |  ----           |
| time        | datetime             |  Period start time    |
| open        | float             |  Open price    |
| high        | float             |  The highest price of the period    |
| low        | float             |  The lowest price of the period    |
| close        | float             |  Close price    |
| tick_volume        | int            |  Tick volume    |
| spread        | int            |  Spread   |
| real_volume        | int            |  Trade volume    |

