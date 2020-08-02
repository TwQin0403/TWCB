TWCB
========================

This simple project is the third party api for Taiwan central bank database(TWCB)

這是第三方央行資料庫的python API。

## 安裝(installation)
```
pip install TWCB
```

## Usage

TWCB support two way to retrieve the data.

API支援兩種方法抓取資料

### Retrieving Data

如果知道要抓那張表，API會根據要抓的表的代碼回傳一個pandas.DataFrame格式的表資料回來。

```python
import TWCB

data = TWCB.get('BP01D01.px')
data.head()
```

### Retrieving Data by Search

也可以根據資料庫中的關鍵字進行搜尋，API會回傳有包含關鍵字的所有表(the list of panda.DataFrame)。

```python
import TWCB

data_list = TWCB.get_by_search('美元之匯率')

```
