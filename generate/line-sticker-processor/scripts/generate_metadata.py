#!/usr/bin/env python3
"""
LINE Sticker Metadata Generator - 生成 LINE 貼圖的標題和說明
"""

import os
import sys
import json


def analyze_sticker_content(sticker_files, descriptions=None):
    """
    分析貼圖內容並生成建議的標題和說明
    
    Args:
        sticker_files: 貼圖檔案路徑列表
        descriptions: 每個貼圖的描述（如果有的話）
    
    Returns:
        建議的中英文標題和說明
    """
    # 這個函數可以根據實際需求擴展，
    # 例如使用 OCR 讀取圖片中的文字，
    # 或者根據檔案名稱和順序生成建議
    
    sticker_count = len(sticker_files)
    
    # 生成基本建議
    suggestions = {
        'title': {
            'en': 'Cute Couple Daily Life',
            'zh': '可愛情侶日常生活'
        },
        'description': {
            'en': f'A set of {sticker_count} adorable stickers featuring a couple\'s everyday moments. Perfect for expressing love, affection, and daily emotions!',
            'zh': f'一組 {sticker_count} 張可愛貼圖，描繪情侶的日常時刻。完美表達愛意、親密感和日常情緒！'
        },
        'sticker_info': []
    }
    
    # 如果有提供描述，則整合進來
    if descriptions:
        for i, desc in enumerate(descriptions, 1):
            suggestions['sticker_info'].append({
                'index': i,
                'file': os.path.basename(sticker_files[i-1]) if i <= len(sticker_files) else None,
                'description': desc
            })
    
    return suggestions


def generate_metadata_file(suggestions, output_path):
    """
    生成 metadata JSON 檔案
    
    Args:
        suggestions: 建議的標題和說明
        output_path: 輸出檔案路徑
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(suggestions, f, ensure_ascii=False, indent=2)
    
    print(f"Metadata 已儲存至: {output_path}")


def print_suggestions(suggestions):
    """
    印出建議的標題和說明
    
    Args:
        suggestions: 建議的標題和說明字典
    """
    print("\n=== LINE 貼圖標題和說明建議 ===\n")
    
    print("英文標題 (English Title):")
    print(f"  {suggestions['title']['en']}")
    print()
    
    print("中文標題 (Chinese Title):")
    print(f"  {suggestions['title']['zh']}")
    print()
    
    print("英文說明 (English Description):")
    print(f"  {suggestions['description']['en']}")
    print()
    
    print("中文說明 (Chinese Description):")
    print(f"  {suggestions['description']['zh']}")
    print()
    
    if suggestions.get('sticker_info'):
        print("\n個別貼圖資訊:")
        for info in suggestions['sticker_info']:
            print(f"  貼圖 {info['index']}: {info.get('description', 'N/A')}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("使用方式: python generate_metadata.py <貼圖目錄或檔案列表>")
        print("範例: python generate_metadata.py stickers/*.png")
        sys.exit(1)
    
    # 收集所有貼圖檔案
    sticker_files = sys.argv[1:]
    sticker_files = [f for f in sticker_files if f.endswith('.png')]
    
    if not sticker_files:
        print("錯誤: 沒有找到 PNG 貼圖檔案")
        sys.exit(1)
    
    print(f"分析 {len(sticker_files)} 個貼圖...")
    
    # 生成建議
    suggestions = analyze_sticker_content(sticker_files)
    
    # 印出建議
    print_suggestions(suggestions)
    
    # 儲存為 JSON
    output_json = 'sticker_metadata.json'
    generate_metadata_file(suggestions, output_json)
