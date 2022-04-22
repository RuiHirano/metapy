---
sidebar_position: 1
---

# Order Methods

## OrderSend

### Example
```
symbol = "EURUSD"
order_type = 0 # BUY
volume = 0.1
price = 1.143321
slippage = 3
stoploss = 1.142232
takeprofit = 1.145542
ticket_id = OrderSend(symbol, order_type, volume, price, slippage, stoploss, takeprofit)
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| symbol      | str             |           | Trade symbol   |
| type        | ENUM_ORDER_TYPE |           | Order type   |
| volume      | float           |           | Requested volume for a deal in lots   |
| price       | float           |           | Price   |
| slippage    | int             |           | Maximal possible deviation from the requested price   |
| stoploss    | float           |           | Stop Loss level of the order  |
| takeprofit  | float           |           | Take Profit level of the order   |
| comment     | str             |  None     | Order comment   |
| magic       | int             |   0       | Expert Advisor ID (magic number)   |
| expiration  | int             |   0       | Order expiration time   |

### Return
Returns number of the ticket assigned to the order by the trade server or -1 if it fails.

|  Name       |  Type    |  Default  |  Description   |
| ----        | ----     | ----      | ----          |
| ticket      | int      |           |  Returns number of the ticket assigned to the order by the trade server or -1 if it fails.  |

## OrderClose

### Example
```
ticket = 1111111
volume = 0.1
price = 1.143321
slippage = 3
closed = OrderClose(ticket, volume, price, slippage)
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| ticket      | int             |           | Order ticket.   |
| volume      | float           |           | Requested volume for a deal in lots   |
| price       | float           |           | Price   |
| slippage    | int             |           | Maximal possible deviation from the requested price   |

### Return
Returns true if successful, otherwise false.

|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| closed      | bool            |           | Returns true if successful, otherwise false.  |

## OrderModify

### Example
```
ticket = 1111111
price = 1.143321
stoploss = 1.142232
takeprofit = 1.145542
modified = OrderModify(ticket, price, stoploss, takeprofit)
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| ticket      | int             |           | Order ticket.   |
| price       | float           |           | Price   |
| stoploss    | float           |           | Stop Loss level of the order  |
| takeprofit  | float           |           | Take Profit level of the order   |
| expiration  | int             |   0       | Order expiration time   |

### Return
Returns true if successful, otherwise false. 

|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| modified      | bool            |           | Returns true if successful, otherwise false.   |


## OrderDelete

### Example
```
ticket = 1111111
deleted = OrderDelete(ticket)
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| ticket      | int             |           | Order ticket.   |

### Return
Returns true if successful, otherwise false. 

|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| deleted      | bool            |           | Returns true if successful, otherwise false.   |