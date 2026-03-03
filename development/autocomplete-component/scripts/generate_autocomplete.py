#!/usr/bin/env python3
"""
自動補完元件生成器

用法：
  python generate_autocomplete.py <output-file> [options]

選項：
  --theme <dark|light>              主題選擇（預設：dark）
  --data-source <api|json|static>   資料來源類型（預設：api）
  --api-endpoint <path>             API 端點路徑（預設：/api/items/search）
  --id-field <field>                ID 欄位名稱（預設：id）
  --primary-field <field>           主要顯示欄位（預設：name）
  --secondary-field <field>         次要顯示欄位（預設：description）
  --label <text>                    輸入框標籤（預設：Search）
  --placeholder <text>              輸入框提示文字（預設：Type to search...）
  --component-id <id>               元件 ID（預設：1）

範例：
  # 基本使用（深色主題）
  python generate_autocomplete.py autocomplete.html
  
  # 淺色主題
  python generate_autocomplete.py autocomplete.html --theme light
  
  # 自訂欄位
  python generate_autocomplete.py stock-search.html \\
    --id-field code \\
    --primary-field code \\
    --secondary-field name \\
    --api-endpoint /api/stocks/search
"""
import argparse
from pathlib import Path
import sys


# Theme configurations
THEMES = {
    'dark': {
        'LABEL_COLOR': 'text-slate-300',
        'INPUT_BG': 'bg-slate-700',
        'INPUT_BORDER': 'border-slate-600',
        'DROPDOWN_BG': 'bg-slate-800',
        'DROPDOWN_BORDER': 'border-slate-600',
        'HOVER_BG': 'hover:bg-slate-700',
        'ITEM_BORDER': 'border-slate-700',
        'ITEM_TEXT_COLOR': 'text-slate-100',
        'HIGHLIGHT_COLOR': 'text-teal-400',
        'ITEM_SECONDARY_COLOR': 'text-slate-400',
        'ITEM_META_COLOR': 'text-slate-500',
        'HELP_TEXT_COLOR': 'text-slate-400',
        'PRIMARY_COLOR': 'primary',
        'SCROLLBAR_CLASS': 'autocomplete-scrollbar-dark',
        'SCROLLBAR_TRACK': '#1e293b',
        'SCROLLBAR_THUMB': '#475569',
        'SCROLLBAR_THUMB_HOVER': '#64748b',
    },
    'light': {
        'LABEL_COLOR': 'text-gray-700',
        'INPUT_BG': 'bg-white',
        'INPUT_BORDER': 'border-gray-300',
        'DROPDOWN_BG': 'bg-white',
        'DROPDOWN_BORDER': 'border-gray-300',
        'HOVER_BG': 'hover:bg-gray-100',
        'ITEM_BORDER': 'border-gray-200',
        'ITEM_TEXT_COLOR': 'text-gray-900',
        'HIGHLIGHT_COLOR': 'text-blue-600',
        'ITEM_SECONDARY_COLOR': 'text-gray-600',
        'ITEM_META_COLOR': 'text-gray-500',
        'HELP_TEXT_COLOR': 'text-gray-500',
        'PRIMARY_COLOR': 'blue-500',
        'SCROLLBAR_CLASS': 'autocomplete-scrollbar-light',
        'SCROLLBAR_TRACK': '#f3f4f6',
        'SCROLLBAR_THUMB': '#d1d5db',
        'SCROLLBAR_THUMB_HOVER': '#9ca3af',
    }
}


def generate_search_logic(data_source: str, api_endpoint: str) -> str:
    """Generate search logic based on data source"""
    
    if data_source == 'api':
        return f"""
                const response = await fetch(`{api_endpoint}?q=${{encodeURIComponent(value)}}`);
                this.suggestions = await response.json();
        """.strip()
    
    elif data_source == 'static':
        return """
                // Static data - replace with your data
                const allItems = [
                    { id: 1, name: 'Item 1', description: 'First item' },
                    { id: 2, name: 'Item 2', description: 'Second item' },
                ];
                
                const query = value.toLowerCase();
                this.suggestions = allItems.filter(item => 
                    item.name.toLowerCase().includes(query) ||
                    item.description.toLowerCase().includes(query)
                ).slice(0, 10);
        """.strip()
    
    elif data_source == 'json':
        return """
                // Load from JSON file
                const response = await fetch('/data/items.json');
                const allItems = await response.json();
                
                const query = value.toLowerCase();
                this.suggestions = allItems.filter(item => 
                    item.name.toLowerCase().includes(query) ||
                    item.description.toLowerCase().includes(query)
                ).slice(0, 10);
        """.strip()
    
    return ""


def generate_autocomplete(
    output_file: Path,
    theme: str = 'dark',
    data_source: str = 'api',
    api_endpoint: str = '/api/items/search',
    id_field: str = 'id',
    primary_field: str = 'name',
    secondary_field: str = 'description',
    label: str = 'Search',
    placeholder: str = 'Type to search...',
    help_text: str = '💡 Start typing to see suggestions',
    component_id: str = '1',
    min_search_length: int = 1,
):
    """生成自動補完元件"""
    
    # 取得模板
    script_dir = Path(__file__).parent
    template_file = script_dir.parent / "assets" / "autocomplete-template.html"
    
    if not template_file.exists():
        print(f"❌ Error: Template file not found at {template_file}")
        sys.exit(1)
    
    # 讀取模板
    template = template_file.read_text(encoding='utf-8')
    
    # 取得主題配置
    if theme not in THEMES:
        print(f"❌ Error: Unknown theme '{theme}'. Available: {', '.join(THEMES.keys())}")
        sys.exit(1)
    
    theme_config = THEMES[theme]
    
    # 生成搜尋邏輯
    search_logic = generate_search_logic(data_source, api_endpoint)
    
    # 替換 placeholder
    replacements = {
        'THEME': theme,
        'DATA_SOURCE': data_source,
        'COMPONENT_ID': component_id,
        'LABEL_TEXT': label,
        'PLACEHOLDER': placeholder,
        'HELP_TEXT': help_text,
        'ID_FIELD': id_field,
        'PRIMARY_FIELD': primary_field,
        'SECONDARY_FIELD': secondary_field,
        'TERTIARY_TEMPLATE': f"item.{secondary_field}",  # Can be customized
        'META_FIELD': 'category',  # Default meta field
        'SEARCH_LOGIC': search_logic,
        'MIN_SEARCH_LENGTH': str(min_search_length),
        **theme_config
    }
    
    # 替換所有 placeholder（按長度降序排序，避免短 placeholder 被先替換導致長 placeholder 失效）
    output = template
    for key in sorted(replacements.keys(), key=len, reverse=True):
        output = output.replace(key, replacements[key])
    
    # 寫入輸出檔案
    output_file.write_text(output, encoding='utf-8')
    
    print(f"✅ Autocomplete component generated: {output_file}")
    print()
    print("📝 Usage:")
    print("   1. Include the generated HTML in your page")
    print("   2. Make sure Alpine.js is loaded:")
    print("      <script defer src=\"https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js\"></script>")
    print()
    print("🎨 Customization:")
    print(f"   - Theme: {theme}")
    print(f"   - Data source: {data_source}")
    print(f"   - API endpoint: {api_endpoint}")
    print()
    print("📡 Events:")
    print(f"   - Listen to 'item-selected' event: @item-selected=\"handleSelection\"")
    print(f"   - Or define: window.on{component_id}Select = (item) => {{ ... }}")


def main():
    parser = argparse.ArgumentParser(
        description="自動補完元件生成器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  python generate_autocomplete.py autocomplete.html
  python generate_autocomplete.py autocomplete.html --theme light
  python generate_autocomplete.py stock-search.html --id-field code --primary-field code --secondary-field name
        """
    )
    
    parser.add_argument("output_file", type=Path, help="輸出檔案路徑")
    parser.add_argument("--theme", choices=['dark', 'light'], default='dark', help="主題（預設：dark）")
    parser.add_argument("--data-source", choices=['api', 'json', 'static'], default='api', help="資料來源（預設：api）")
    parser.add_argument("--api-endpoint", default='/api/items/search', help="API 端點（預設：/api/items/search）")
    parser.add_argument("--id-field", default='id', help="ID 欄位（預設：id）")
    parser.add_argument("--primary-field", default='name', help="主要欄位（預設：name）")
    parser.add_argument("--secondary-field", default='description', help="次要欄位（預設：description）")
    parser.add_argument("--label", default='Search', help="標籤文字（預設：Search）")
    parser.add_argument("--placeholder", default='Type to search...', help="提示文字（預設：Type to search...）")
    parser.add_argument("--help-text", default='💡 Start typing to see suggestions', help="說明文字")
    parser.add_argument("--component-id", default='1', help="元件 ID（預設：1）")
    parser.add_argument("--min-search-length", type=int, default=1, help="最小搜尋長度（預設：1）")
    
    args = parser.parse_args()
    
    generate_autocomplete(
        output_file=args.output_file,
        theme=args.theme,
        data_source=args.data_source,
        api_endpoint=args.api_endpoint,
        id_field=args.id_field,
        primary_field=args.primary_field,
        secondary_field=args.secondary_field,
        label=args.label,
        placeholder=args.placeholder,
        help_text=args.help_text,
        component_id=args.component_id,
        min_search_length=args.min_search_length,
    )


if __name__ == "__main__":
    main()
