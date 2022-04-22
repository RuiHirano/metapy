---
sidebar_position: 1
---

# Metapy


## Example
```
runner = MetaPy(
    server="http://localhost:5005"
    expert_advisor=MyEA,
    debug=True,
    use_backtesting=False,
    log_level="DEBUG"
)
runner.run()
```

## Props
|  Name       |  Type           |  Default  |  Description   |
| ----        | ----            | ----      | ----           |
| server  | str  |      | Server address  |
| expert_advisor  | ExpertAdvisor  |      | ExpertAdvisor class. not a instance.  |
| debug  | bool  | False     | Flag of debug mode.  |
| use_backtesting  | bool  | False     | Flag of using backtesting.py instead of metatrader EA.  |
| log_level  | str  | "INFO"     | Log level.  |
