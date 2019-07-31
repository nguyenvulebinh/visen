# ViSen
ViSen is library to format tone of Vietnamese sentences

## Install
```bash
pip install visen
```


## Usage
```python
>>> import visen
>>> visen.clean_tone('gía cả thị trừơng?')
'giá cả thị trường?'
>>> visen.remove_tone('công việc')
'cong viec'
```