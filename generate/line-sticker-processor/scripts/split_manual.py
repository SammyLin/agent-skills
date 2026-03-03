#!/usr/bin/env python3
"""
Manual LINE Sticker Splitter - 手動切割 LINE 貼圖
適用於已知網格佈局的情況
"""

import os
import sys
from PIL import Image


def split_grid_manual(image_path, output_dir, rows, cols, padding=0):
    """
    手動切割網格佈局的貼圖
    
    Args:
        image_path: 輸入圖片路徑
        output_dir: 輸出目錄
        rows: 行數
        cols: 列數
        padding: 每個格子之間的間距（像素）
    
    Returns:
        切割後的圖片路徑列表
    """
    img = Image.open(image_path).convert('RGBA')
    width, height = img.size
    
    # 計算每個格子的大小
    cell_width = (width - padding * (cols - 1)) // cols
    cell_height = (height - padding * (rows - 1)) // rows
    
    os.makedirs(output_dir, exist_ok=True)
    sticker_files = []
    
    index = 1
    for row in range(rows):
        for col in range(cols):
            # 計算切割位置
            left = col * (cell_width + padding)
            top = row * (cell_height + padding)
            right = left + cell_width
            bottom = top + cell_height
            
            # 切割圖片
            sticker = img.crop((left, top, right, bottom))
            
            # 儲存
            output_path = os.path.join(output_dir, f'sticker_{index:02d}.png')
            sticker.save(output_path, 'PNG')
            sticker_files.append(output_path)
            
            index += 1
    
    return sticker_files


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("使用方式: python split_manual.py <輸入圖片> <輸出目錄> <行數> <列數> [間距]")
        print("範例: python split_manual.py input.png output 4 3 10")
        sys.exit(1)
    
    input_image = sys.argv[1]
    output_dir = sys.argv[2]
    rows = int(sys.argv[3])
    cols = int(sys.argv[4])
    padding = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    
    files = split_grid_manual(input_image, output_dir, rows, cols, padding)
    print(f"切割完成！生成 {len(files)} 個貼圖")
    for f in files:
        print(f"  - {f}")
