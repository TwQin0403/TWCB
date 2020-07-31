TWCB
========================

This simple project is the third party api for Taiwan central bank database(TWCB)



## Usage
### Retrieving Data
```python
import TWCB

data = TWCB.get('BP01D01.px')
data.head()

```

### Retrieving Data by Search

```python
import TWCB

data_list = TWCB.get_by_search('美元之匯率')

```
