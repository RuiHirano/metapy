---
sidebar_position: 1
---

# Metapy


## Example
```
class MyEA(ExpertAdvisor):
    def on_init(self):
        print("on_init")  

    def on_tick(self, tick):
        print("on_tick", tick)

    def on_deinit(self):
        print("on_deinit")
```

## Override Event Functions
|  Name       |  Args     |  Description   |
| ----        | ----        | ----          |
| on_init      |             |  The function is called in indicators and EAs when the Init event occurs. It is used to initialize a running MQL5 program.  |
| on_tick      |   tick: Tick        |  The function is called in EAs when the NewTick event occurs to handle a new quote.  |
| on_deinit      |             |  The function is called in indicators and EAs when the Deinit event occurs. It is used to deinitialize a running MQL5 program.  |

## OnInit
The function is called in indicators and EAs when the Init event occurs. It is used to initialize a running MQL5 program.

### Example
```
class MyEA(ExpertAdvisor):
    def on_init(self):
        print("on_init")  

    ...
```


## OnTick
The function is called in EAs when the NewTick event occurs to handle a new quote.
### Example
```
class MyEA(ExpertAdvisor):
    ...
    def on_tick(self, tick):
        print("on_tick", tick)
```

### Args
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----           |
| tick        | Tick             | ----      | Tick data   |

## OnDeinit
The function is called in indicators and EAs when the Deinit event occurs. It is used to deinitialize a running MQL5 program.

### Example
```
class MyEA(ExpertAdvisor):
    ...
    def on_deinit(self):
        print("on_deinit") 
```
