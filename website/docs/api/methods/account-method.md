---
sidebar_position: 3
---

# Account Methods

## AccountBalance
Returns balance value of the current account.

### Example
```
balance = AccountBalance()
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |

### Return
Balance value of the current account (the amount of money on the account).

|  Name       |  Type    |  Default  |  Description   |
| ----        | ----     | ----      | ----          |
| balance      | float      |           |  Balance value of the current account (the amount of money on the account).  |


## AccountCredit
Returns credit value of the current account.

### Example
```
credit = AccountCredit()
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |

### Return
Credit value of the current account (the amount of money on the account).

|  Name       |  Type    |  Default  |  Description   |
| ----        | ----     | ----      | ----          |
| credit      | float      |           |  Credit value of the current account (the amount of money on the account).  |

## AccountCurrency
Returns currency name of the current account.

### Example
```
currency = AccountCurrency()
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |

### Return
Currency name of the current account.

|  Name       |  Type    |  Default  |  Description   |
| ----        | ----     | ----      | ----          |
| currency      | str      |           |  Currency name of the current account.  |

## AccountEquity
Returns equity value of the current account.

### Example
```
equity = AccountEquity()
```

### Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----          |

### Return
Equity value of the current account. Equity calculation depends on trading server settings.

|  Name       |  Type    |  Default  |  Description   |
| ----        | ----     | ----      | ----          |
| equity      | float    |           |  Equity value of the current account. Equity calculation depends on trading server settings.  |
