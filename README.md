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

status = FlagWord(["pending", "approved", "actioned"])

status.set(status.approved)
status.has(status.approved)  # True
status.has(status.actioned)  # False

```

