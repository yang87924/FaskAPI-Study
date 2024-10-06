# FastAPI 專案設置指南

## 簡介
這是一個使用 FastAPI 框架開發的 Python Web 應用程序。本文檔將指導您如何設置和運行此專案。

## 環境要求
- Python 3.7 或更高版本
- pip（Python 包管理器）

## 安裝步驟

### 1. 創建虛擬環境
首先，在專案目錄中創建一個 Python 虛擬環境：
```bash
python -m venv venv
```

### 2. 激活虛擬環境
在 Windows PowerShell 中：
```bash
.\venv\Scripts\activate
```
在 Linux 或 macOS 中：
```bash
source venv/bin/activate
```

### 3. 安裝依賴包
使用 pip 安裝所需的依賴包：
```bash
pip install -r requirements.txt
```

## 運行應用

啟動開發服務器：
```bash
uvicorn main:app --reload
```

- `main`: 表示 Python 模組 `main.py`
- `app`: 表示在 `main.py` 中創建的 FastAPI 實例
- `--reload`: 啟用熱重載，當代碼變更時自動重啟服務器

## API 文檔
啟動服務器後，您可以訪問以下URL查看自動生成的API文檔：
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 專案結構
```
.
├── Controller/           # 控制器目錄
│   ├── userController.py
│   └── articleController.py
├── models/               # 模型目錄
│   ├── user.py
│   └── article.py
├── repository/           # 資料庫操作目錄
│   ├── userRepository.py
│   └── articleRepository.py
├── schemas/              # Pydantic 模式目錄
│   ├── user.py
│   └── article.py
├── service/              # 服務層目錄
│   ├── userService.py
│   └── articleService.py
├── .env                  # 環境變量文件
├── .env.example          # 環境變量範例文件
├── .gitignore            # Git 忽略文件
├── database.py           # 資料庫連接設置
├── main.py               # 主應用程序文件
├── requirements.txt      # 項目依賴列表
└── README.md             # 本文檔
```

## 注意事項
- 確保在運行任何命令之前已激活虛擬環境
- 建議在開發環境中使用 `--reload` 選項，但在生產環境中應移除此選項

## 貢獻指南
歡迎提交 Pull Requests 和 Issues！

## 許可證
[選擇合適的許可證，例如：MIT、Apache 2.0 等]
