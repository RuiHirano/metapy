---
sidebar_position: 3
---

# Enums

## ENUM_ORDER_TYPE
When sending a trade request using the OrderSend() function, some operations require the indication of the order type. The order type can accept values of the ENUM_ORDER_TYPE enumeration.

### Properties
|  Name                 |  Type   |  Value |  Description   |
| ----                  | ----    | ----   | ----          |
| ORDER_TYPE_BUY        | int     | 0      | Market Buy order         |
| ORDER_TYPE_SELL       | int     | 1      | Market Sell order        |
| ORDER_TYPE_BUY_LIMIT  | int     | 2      | Buy Limit pending order  |
| ORDER_TYPE_SELL_LIMIT | int     | 3      | Sell Limit pending order |
| ORDER_TYPE_BUY_STOP   | int     | 4      | Buy Stop pending order   |
| ORDER_TYPE_SELL_STOP  | int     | 5      | Sell Stop pending order  |

## ENUM_TIMEFRAME
All predefined timeframes of charts have unique identifiers. The PERIOD_CURRENT identifier means the current period of a chart, at which a mql5-program is running.

### Properties
|  Name            |  Type   |  Value |  Description   |
| ----             | ----    | ----   | ----          |
| PERIOD_CURRENT   | int     | 0      | Current timeframe |
| PERIOD_M1        | int     | 1      | 1 minute |
| PERIOD_M5        | int     | 5      | 5 minute |
| PERIOD_M15       | int     | 15     | 15 minute |
| PERIOD_M30       | int     | 30     | 30 minute |
| PERIOD_H1        | int     | 60     | 1 hour |
| PERIOD_H4        | int     | 240    | 1 hours |
| PERIOD_D1        | int     | 1440   | 1 day |
| PERIOD_W1        | int     | 10080  | 1 week |
| PERIOD_MN1       | int     | 43200  | 1 month |
