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

### Retrieving the reference table

可以使用get_info指令來獲得表的名子與對應的code的參照表，在使用套件時也會在當前目錄產生reference.csv參照表

```python
import TWCB

info = TWCB.get_info()

```

### Retrieving all the data at the current time
version 0.1.2支援下載目前的所有資料，會在當前目錄產生一個名為download_TWCB.json的檔案

```python
import TWCB

TWCB.get_all()

```

#### How to load the data
檔案的格式會長成表的中文名對應表格的json結構，可用下列程式還原為表名:pandas.DataFrame的字典結構

```python
with open('download_TWCB.json','r',encoding='utf-8') as f:
    test_data = json.load(f)

test_data = {key:pd.read_json(test_data[key]) for key in test_data.keys()} 
```