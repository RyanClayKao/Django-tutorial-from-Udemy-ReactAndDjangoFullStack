# Django 專案要 git版本控制時，記得要產出 requirements.txt，作為還原的依據
------
## 建立 requirements.txt
1. 輸入
    ``` python
    pip freeze > requirements.txt
    ```

## 從 github上 clone回來
------
1.使用
    ``` python
    pip install -r requirements.txt
    ```