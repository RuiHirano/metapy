---
sidebar_position: 2
---

# TimeSeries Methods

## GetNRatesByStartPosition
Call by the first position and the number of required elements
### Example
```
symbol = "EURUSD"
timeframe = 0
start_pos = 0
count = 100
rates = GetNRatesByStartPosition(symbol, timeframe, start_pos, count)
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| symbol  | str             |           | Trade symbol   |
| timeframe        | ENUM_TIMEFRAME |           | Period   |
| start_pos      | int           |           | Start position   | 
| count       | int           |           | data count to get   |

### Return
Returns list of the Rate.

|  Name       |  Type    |  Default  |  Description   |
| ----        | ----     | ----      | ----          |
| rates      | Rate[]      |           |  Returns list of the Rate  |

## GetNRatesByStartTime
Call by the start date and the number of required elements

### Example
```
from datetime import datetime

symbol = "EURUSD"
timeframe = 0
start_time = datetime.now()
count = 100
rates = GetNRatesByStartTime(symbol, timeframe, start_time, count)
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| symbol  | str             |           | Trade symbol   |
| timeframe        | ENUM_TIMEFRAME |           | Period   |
| start_time      | datetime           |           | Start date and time   | 
| count       | int           |           | data count to get   |

### Return
Returns list of the Rate.

|  Name       |  Type    |  Default  |  Description   |
| ----        | ----     | ----      | ----          |
| rates      | Rate[]      |           |  Returns list of the Rate  |

## GetRatesByTimeInterval
Call by the start and end dates of a required time interval

### Example
```
from datetime import datetime, timedelta

symbol = "EURUSD"
timeframe = 0
start_time = datetime.now()
stop_time = start_time  + datetime.timedelta(days=-1)
rates = GetRatesByTimeInterval(symbol, timeframe, start_time, stop_time)
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |
| symbol  | str             |           | Trade symbol   |
| timeframe        | ENUM_TIMEFRAME |           | Period   |
| start_time      | datetime           |           | Start date and time   | 
| stop_time       | datetime           |           | End date and time   |

### Return
Returns list of the Rate.

|  Name       |  Type    |  Default  |  Description   |
| ----        | ----     | ----      | ----          |
| rates      | Rate[]      |           |  Returns list of the Rate  |