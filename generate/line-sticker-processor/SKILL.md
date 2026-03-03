---
name: line-sticker-processor
description: 處理 LINE 貼圖的完整工具，包含圖片切割、去背、調整大小和 metadata 生成。當用戶需要處理 LINE 貼圖圖片時使用，包括：(1) 從組合圖中切割個別貼圖, (2) 去除背景並設為透明, (3) 調整為 LINE 規格尺寸 (主畫面圖 240x240、聊天小圖示 96x74、貼圖 370x320), (4) 生成中英文標題和說明建議。Do not use for: 設計貼圖原稿、非 LINE 平台貼圖（Telegram/WhatsApp）、動態貼圖、或一般圖片編輯。
---

# LINE 貼圖處理工具

這個 skill 提供完整的 LINE 貼圖處理流程，從圖片處理到 metadata 生成。

## 主要功能

1. **圖片切割**: 從包含多個小圖的組合圖中切割出個別貼圖
2. **去背處理**: 移除白色或單色背景，設為透明
3. **尺寸調整**: 按照 LINE 規格調整圖片大小
4. **Metadata 生成**: 自動生成中英文標題和說明建議

## 快速開始

### 處理已切割好的貼圖

如果你已經有個別的貼圖檔案（每張都是獨立的 PNG 檔案），使用整合處理腳本：

```bash
python scripts/line_sticker_processor.py sticker_*.png output/
```

或處理整個目錄：

```bash
python scripts/line_sticker_processor.py input_directory/ output/
```

### 處理組合圖（需手動切割）

如果你有一張包含多個貼圖的組合圖，先使用手動切割工具：

```bash
# 例如：4 行 3 列的網格佈局，每個格子間距 10 像素
python scripts/split_manual.py combo.png temp_output/ 4 3 10
```

然後再使用整合處理腳本處理切割後的圖片。

## 輸出結構

處理完成後會生成以下目錄結構：

```
output/
├── 01_main/
│   └── main.png          # 主畫面圖 (240x240)
├── 02_tab/
│   └── tab.png           # 聊天小圖示 (96x74)
├── 03_stickers/
│   ├── 01.png           # 貼圖 1 (370x320)
│   ├── 02.png           # 貼圖 2 (370x320)
│   └── ...
└── metadata.json        # 標題和說明建議
```

## LINE 貼圖規格

詳細規格請參考 `references/line_specs.md`。主要要求：

- **主畫面圖**: 240 x 240 像素
- **聊天小圖示**: 96 x 74 像素
- **貼圖圖片**: 370 x 320 像素
- **格式**: PNG，透明背景
- **解析度**: 72 DPI 以上
- **檔案大小**: 每張小於 1MB
- **尺寸要求**: 必須為偶數

## 工作流程

1. **準備圖片**: 確保有高品質的原始圖片
2. **切割（如需要）**: 使用 `split_manual.py` 切割組合圖
3. **處理**: 使用 `line_sticker_processor.py` 進行去背和調整大小
4. **檢查**: 確認所有圖片符合規格
5. **使用 metadata**: 參考生成的標題和說明建議

## 進階使用

### 手動調整去背參數

如果自動去背效果不理想，可以修改 `line_sticker_processor.py` 中的 `fuzz` 參數（預設 15%）：

```python
def remove_white_background(image_path, output_path, fuzz='20%'):  # 調整這裡
    ...
```

### 自訂 Metadata

編輯 `line_sticker_processor.py` 中的 `analyze_and_suggest_metadata` 函數，自訂標題和說明的生成邏輯。

## 提示和技巧

1. **圖片品質**: 使用高解析度原始圖片可獲得更好的結果
2. **背景顏色**: 純白色背景最容易去除
3. **圖片大小**: 確保原始圖片足夠大，縮小比放大效果好
4. **檢查透明度**: 處理後檢查透明背景是否完整
5. **檔案大小**: 如果超過 1MB，考慮降低圖片品質或簡化設計

## 故障排除

### 去背效果不佳
- 調整 `fuzz` 參數（5%-30%）
- 手動使用圖片編輯軟體處理

### 圖片太大
- 使用 PNG 壓縮工具
- 簡化圖片設計
- 減少顏色數量

### 切割不準確
- 檢查組合圖的網格是否規則
- 調整切割參數（行數、列數、間距）
- 考慮手動切割
