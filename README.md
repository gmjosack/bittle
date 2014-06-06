# bittle

### Description

Bittle is a simple module to help me to things with bits.

### Installation

New versions will be updated to PyPI pretty regularly so it should be as easy
as:

```bash
pip install bittle
```

### Examples

```python

from bittle import FlagWord

Status = FlagWord(["pending", "approved", "actioned"])

status = Status()
status.set(status.approved)
status.has(Status.approved)  # True
status.has("actioned")  # False

```

