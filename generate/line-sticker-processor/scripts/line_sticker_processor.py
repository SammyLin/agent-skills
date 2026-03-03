#!/usr/bin/env python3
"""
LINE Sticker Complete Processor - 完整的 LINE 貼圖處理工具
整合切割、去背、調整大小和 metadata 生成
"""

import os
import sys
import subprocess
from PIL import Image
import json


def ensure_even_size(size):
    """確保尺寸為偶數"""
    return size - (size % 2)


def trim_transparent(image_path, output_path):
    """修剪透明邊界"""
    subprocess.run([
        'convert', image_path,
        '-trim',
        '+repage',
        output_path
    ], check=True)


def remove_white_background(image_path, output_path, fuzz='15%'):
    """去除白色背景並設為透明"""
    subprocess.run([
        'convert', image_path,
        '-fuzz', fuzz,
        '-transparent', 'white',
        '-alpha', 'set',
        output_path
    ], check=True)


def resize_with_padding(image_path, output_path, target_size):
    """調整圖片大小並維持長寬比，多餘空間填充透明"""
    img = Image.open(image_path).convert('RGBA')
    
    target_width = ensure_even_size(target_size[0])
    target_height = ensure_even_size(target_size[1])
    
    # 計算縮放比例
    img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
    
    # 創建透明畫布
    canvas = Image.new('RGBA', (target_width, target_height), (0, 0, 0, 0))
    
    # 置中貼上
    offset = ((target_width - img.width) // 2, (target_height - img.height) // 2)
    canvas.paste(img, offset, img)
    
    # 儲存，設定 DPI 為 72
    canvas.save(output_path, 'PNG', dpi=(72, 72), optimize=True)
    
    # 檢查檔案大小
    file_size = os.path.getsize(output_path)
    if file_size > 1024 * 1024:
        print(f"  ⚠️  警告: {os.path.basename(output_path)} 大小 {file_size/1024:.1f}KB 超過 1MB")
        return False
    return True


def process_single_sticker(input_path, output_dir, index, is_first=False):
    """
    處理單一貼圖
    
    Args:
        input_path: 輸入檔案路徑
        output_dir: 輸出目錄
        index: 貼圖索引（從 1 開始）
        is_first: 是否為第一張（需生成主畫面圖和聊天小圖示）
    
    Returns:
        生成的檔案路徑字典
    """
    results = {}
    temp_dir = os.path.join(output_dir, '.temp')
    os.makedirs(temp_dir, exist_ok=True)
    
    # Step 1: 去背
    nobg_path = os.path.join(temp_dir, f'nobg_{index}.png')
    print(f"  去背處理...")
    remove_white_background(input_path, nobg_path)
    
    # Step 2: 修剪透明邊界
    trimmed_path = os.path.join(temp_dir, f'trimmed_{index}.png')
    print(f"  修剪邊界...")
    trim_transparent(nobg_path, trimmed_path)
    
    # Step 3: 調整為各種尺寸
    if is_first:
        # 主畫面圖 240x240
        main_dir = os.path.join(output_dir, '01_main')
        os.makedirs(main_dir, exist_ok=True)
        main_path = os.path.join(main_dir, 'main.png')
        print(f"  生成主畫面圖 (240x240)...")
        resize_with_padding(trimmed_path, main_path, (240, 240))
        results['main'] = main_path
        
        # 聊天小圖示 96x74
        tab_dir = os.path.join(output_dir, '02_tab')
        os.makedirs(tab_dir, exist_ok=True)
        tab_path = os.path.join(tab_dir, 'tab.png')
        print(f"  生成聊天小圖示 (96x74)...")
        resize_with_padding(trimmed_path, tab_path, (96, 74))
        results['tab'] = tab_path
    
    # 貼圖 370x320
    sticker_dir = os.path.join(output_dir, '03_stickers')
    os.makedirs(sticker_dir, exist_ok=True)
    sticker_path = os.path.join(sticker_dir, f'{index:02d}.png')
    print(f"  生成貼圖 (370x320)...")
    resize_with_padding(trimmed_path, sticker_path, (370, 320))
    results['sticker'] = sticker_path
    
    return results


def analyze_and_suggest_metadata(sticker_count, image_descriptions=None):
    """
    分析並建議 metadata
    
    Args:
        sticker_count: 貼圖數量
        image_descriptions: 圖片描述列表（可選）
    
    Returns:
        metadata 字典
    """
    metadata = {
        'title': {
            'en': 'Cute Couple Stickers',
            'zh': '可愛情侶貼圖'
        },
        'description': {
            'en': f'{sticker_count} adorable stickers for couples to express their love and daily life moments.',
            'zh': f'{sticker_count} 張可愛貼圖，讓情侶表達愛意和日常生活的溫馨時刻。'
        }
    }
    
    if image_descriptions:
        metadata['sticker_descriptions'] = image_descriptions
    
    return metadata


def main():
    """主程式"""
    if len(sys.argv) < 3:
        print("使用方式: python complete_processor.py <輸入檔案或目錄> <輸出目錄>")
        print()
        print("範例:")
        print("  處理單一組合圖: python complete_processor.py combo.png output/")
        print("  處理多個檔案: python complete_processor.py sticker_*.png output/")
        print("  處理目錄: python complete_processor.py input_dir/ output/")
        sys.exit(1)
    
    # 收集輸入檔案
    input_files = []
    for arg in sys.argv[1:-1]:
        if os.path.isfile(arg):
            input_files.append(arg)
        elif os.path.isdir(arg):
            for f in os.listdir(arg):
                if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                    input_files.append(os.path.join(arg, f))
    
    output_dir = sys.argv[-1]
    
    if not input_files:
        print("錯誤: 沒有找到有效的圖片檔案")
        sys.exit(1)
    
    print(f"\n🚀 開始處理 {len(input_files)} 個檔案...")
    print(f"📁 輸出目錄: {output_dir}\n")
    
    os.makedirs(output_dir, exist_ok=True)
    
    # 處理每個檔案
    all_results = []
    for i, input_file in enumerate(input_files, 1):
        print(f"\n處理 {i}/{len(input_files)}: {os.path.basename(input_file)}")
        is_first = (i == 1)
        
        results = process_single_sticker(input_file, output_dir, i, is_first)
        all_results.append(results)
        
        print(f"  ✅ 完成")
    
    # 清理臨時檔案
    import shutil
    temp_dir = os.path.join(output_dir, '.temp')
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    
    # 生成 metadata
    print("\n\n📝 生成 metadata 建議...")
    metadata = analyze_and_suggest_metadata(len(input_files))
    
    metadata_path = os.path.join(output_dir, 'metadata.json')
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    # 印出結果
    print("\n" + "="*60)
    print("✅ 處理完成!")
    print("="*60)
    print(f"\n生成檔案:")
    print(f"  📁 主畫面圖 (240x240): {output_dir}/01_main/main.png")
    print(f"  📁 聊天小圖示 (96x74): {output_dir}/02_tab/tab.png")
    print(f"  📁 貼圖 (370x320): {output_dir}/03_stickers/ ({len(input_files)} 張)")
    print(f"  📄 Metadata: {metadata_path}")
    
    print("\n建議的標題和說明:")
    print(f"\n  英文標題: {metadata['title']['en']}")
    print(f"  中文標題: {metadata['title']['zh']}")
    print(f"\n  英文說明: {metadata['description']['en']}")
    print(f"  中文說明: {metadata['description']['zh']}")
    print()


if __name__ == '__main__':
    main()
