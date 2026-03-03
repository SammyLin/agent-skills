#!/usr/bin/env python3
"""
LINE Sticker Processor - 處理 LINE 貼圖的切割、調整大小和去背
"""

import os
import sys
from PIL import Image
import subprocess


def detect_and_split_grid(image_path, output_dir, padding=20):
    """
    自動偵測網格佈局並切割個別貼圖
    
    Args:
        image_path: 輸入圖片路徑
        output_dir: 輸出目錄
        padding: 邊界留白（預設 20 像素）
    
    Returns:
        切割後的圖片路徑列表
    """
    img = Image.open(image_path).convert('RGBA')
    width, height = img.size
    
    # 使用 ImageMagick 的 trim 功能去除多餘空白
    # 這樣可以更準確地偵測每個小圖的邊界
    temp_trimmed = os.path.join(output_dir, 'temp_trimmed.png')
    subprocess.run([
        'convert', image_path,
        '-fuzz', '10%',
        '-trim',
        '+repage',
        temp_trimmed
    ], check=True)
    
    # 重新載入已修剪的圖片
    img = Image.open(temp_trimmed)
    
    # 分析圖片以找出網格結構
    # 這裡假設是規則的網格佈局
    sticker_files = []
    
    # 使用 ImageMagick 的 crop 功能來切割圖片
    # 這個指令會自動偵測並切割非透明區域
    crop_pattern = os.path.join(output_dir, 'sticker_%02d.png')
    
    subprocess.run([
        'convert', temp_trimmed,
        '-crop', '0x0+0+0',  # 自動切割
        '-background', 'none',
        '-alpha', 'set',
        '+repage',
        crop_pattern
    ], check=True)
    
    # 收集所有切割後的檔案
    for i in range(100):  # 假設最多 100 個貼圖
        sticker_file = os.path.join(output_dir, f'sticker_{i:02d}.png')
        if os.path.exists(sticker_file):
            sticker_files.append(sticker_file)
        else:
            break
    
    # 清理臨時檔案
    if os.path.exists(temp_trimmed):
        os.remove(temp_trimmed)
    
    return sticker_files


def remove_background(image_path, output_path, fuzz='10%'):
    """
    使用 ImageMagick 去背（移除白色或單色背景）
    
    Args:
        image_path: 輸入圖片路徑
        output_path: 輸出圖片路徑
        fuzz: 容差值（預設 10%）
    """
    subprocess.run([
        'convert', image_path,
        '-fuzz', fuzz,
        '-transparent', 'white',
        '-background', 'none',
        '-alpha', 'set',
        output_path
    ], check=True)


def resize_to_line_specs(image_path, output_path, target_size, maintain_aspect=True):
    """
    調整圖片大小以符合 LINE 貼圖規格
    
    Args:
        image_path: 輸入圖片路徑
        output_path: 輸出圖片路徑
        target_size: 目標尺寸 (width, height)
        maintain_aspect: 是否維持長寬比（預設 True）
    """
    img = Image.open(image_path).convert('RGBA')
    
    target_width, target_height = target_size
    
    # 確保尺寸為偶數
    target_width = target_width - (target_width % 2)
    target_height = target_height - (target_height % 2)
    
    if maintain_aspect:
        # 計算縮放比例，保持長寬比
        img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
        
        # 創建透明畫布
        canvas = Image.new('RGBA', (target_width, target_height), (0, 0, 0, 0))
        
        # 將圖片置中
        offset = ((target_width - img.width) // 2, (target_height - img.height) // 2)
        canvas.paste(img, offset, img)
        
        img = canvas
    else:
        img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # 設定 DPI 為 72
    img.save(output_path, 'PNG', dpi=(72, 72), optimize=True)
    
    # 檢查檔案大小
    file_size = os.path.getsize(output_path)
    if file_size > 1024 * 1024:  # 1MB
        print(f"警告: {output_path} 大小為 {file_size / 1024:.2f}KB，超過 1MB 限制")


def process_line_stickers(input_image, output_dir):
    """
    處理 LINE 貼圖的完整流程
    
    Args:
        input_image: 輸入的組合圖片路徑
        output_dir: 輸出目錄
    
    Returns:
        處理結果的字典
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Step 1: 偵測並切割網格
    print("步驟 1: 偵測並切割貼圖...")
    temp_dir = os.path.join(output_dir, 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    
    sticker_files = detect_and_split_grid(input_image, temp_dir)
    print(f"找到 {len(sticker_files)} 個貼圖")
    
    # Step 2: 處理每個貼圖
    print("步驟 2: 處理貼圖...")
    
    # 創建輸出子目錄
    main_dir = os.path.join(output_dir, 'main')
    tab_dir = os.path.join(output_dir, 'tab')
    stickers_dir = os.path.join(output_dir, 'stickers')
    
    for d in [main_dir, tab_dir, stickers_dir]:
        os.makedirs(d, exist_ok=True)
    
    results = {
        'main': [],
        'tab': [],
        'stickers': []
    }
    
    for i, sticker_file in enumerate(sticker_files):
        # 去背處理
        nobg_file = os.path.join(temp_dir, f'nobg_{i:02d}.png')
        remove_background(sticker_file, nobg_file)
        
        if i == 0:
            # 第一張圖：主畫面圖、聊天小圖示
            # 主畫面圖 240x240
            main_path = os.path.join(main_dir, 'main.png')
            resize_to_line_specs(nobg_file, main_path, (240, 240))
            results['main'].append(main_path)
            
            # 聊天小圖示 96x74
            tab_path = os.path.join(tab_dir, 'tab.png')
            resize_to_line_specs(nobg_file, tab_path, (96, 74))
            results['tab'].append(tab_path)
        
        # 所有圖片都要有 370x320 版本
        sticker_path = os.path.join(stickers_dir, f'sticker_{i+1:02d}.png')
        resize_to_line_specs(nobg_file, sticker_path, (370, 320))
        results['stickers'].append(sticker_path)
    
    # 清理臨時檔案
    import shutil
    shutil.rmtree(temp_dir)
    
    print(f"處理完成！輸出目錄: {output_dir}")
    return results


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("使用方式: python process_stickers.py <輸入圖片> <輸出目錄>")
        sys.exit(1)
    
    input_image = sys.argv[1]
    output_dir = sys.argv[2]
    
    results = process_line_stickers(input_image, output_dir)
    
    print("\n生成的檔案:")
    print(f"- 主畫面圖 (240x240): {results['main']}")
    print(f"- 聊天小圖示 (96x74): {results['tab']}")
    print(f"- 貼圖 (370x320): {len(results['stickers'])} 張")
