#!/usr/bin/env python3
"""
FastAPI 專案生成器

用法：
  python generate_project.py <project-name> [options]

選項：
  --description <text>     專案描述（預設：FastAPI Application）
  --output <path>          輸出目錄（預設：當前目錄）
  --no-git                 不初始化 Git repository

範例：
  python generate_project.py my-api
  python generate_project.py my-api --description "My awesome API"
  python generate_project.py my-api --output ~/projects
"""
import argparse
import shutil
from pathlib import Path
import sys


def normalize_project_name(name: str) -> str:
    """將專案名稱正規化為 Python 模組名稱"""
    # 移除特殊字元，只保留英數字和底線
    normalized = "".join(c if c.isalnum() or c == "_" else "_" for c in name.lower())
    # 移除開頭的數字
    if normalized and normalized[0].isdigit():
        normalized = "_" + normalized
    return normalized


def replace_placeholders(file_path: Path, replacements: dict):
    """替換檔案中的 placeholder"""
    if file_path.suffix in ['.py', '.html', '.md', '.txt']:
        content = file_path.read_text(encoding='utf-8')
        for key, value in replacements.items():
            content = content.replace(key, value)
        file_path.write_text(content, encoding='utf-8')


def generate_project(project_name: str, description: str, output_dir: Path, init_git: bool = True):
    """生成 FastAPI 專案"""
    
    # 正規化專案名稱
    normalized_name = normalize_project_name(project_name)
    
    # 專案路徑
    project_dir = output_dir / project_name
    
    # 檢查專案目錄是否已存在
    if project_dir.exists():
        print(f"❌ Error: Directory '{project_dir}' already exists!")
        sys.exit(1)
    
    # 取得模板目錄
    script_dir = Path(__file__).parent
    template_dir = script_dir.parent / "assets" / "template"
    
    if not template_dir.exists():
        print(f"❌ Error: Template directory not found at {template_dir}")
        sys.exit(1)
    
    print(f"📦 Generating FastAPI project: {project_name}")
    print(f"   Location: {project_dir}")
    print(f"   Description: {description}")
    print()
    
    # 複製模板
    print("📋 Copying template files...")
    shutil.copytree(template_dir, project_dir)
    
    # 替換 placeholder
    print("✏️  Replacing placeholders...")
    replacements = {
        "{PROJECT_NAME}": project_name,
        "{PROJECT_DESCRIPTION}": description,
    }
    
    # 遞迴替換所有檔案中的 placeholder
    for file_path in project_dir.rglob("*"):
        if file_path.is_file():
            replace_placeholders(file_path, replacements)
    
    # 初始化 Git（如果需要）
    if init_git:
        print("🔧 Initializing Git repository...")
        import subprocess
        try:
            subprocess.run(["git", "init"], cwd=project_dir, check=True, capture_output=True)
            subprocess.run(["git", "add", "."], cwd=project_dir, check=True, capture_output=True)
            subprocess.run(
                ["git", "commit", "-m", "Initial commit"],
                cwd=project_dir,
                check=True,
                capture_output=True
            )
            print("   ✅ Git repository initialized")
        except subprocess.CalledProcessError as e:
            print(f"   ⚠️  Git initialization failed: {e}")
        except FileNotFoundError:
            print("   ⚠️  Git not found, skipping Git initialization")
    
    print()
    print("✅ Project generated successfully!")
    print()
    print("📝 Next steps:")
    print(f"   cd {project_name}")
    print("   python -m venv venv")
    print("   source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
    print("   pip install -r requirements.txt")
    print("   python -m app.main")
    print()
    print("🌐 Then open: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")


def main():
    parser = argparse.ArgumentParser(
        description="FastAPI 專案生成器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  python generate_project.py my-api
  python generate_project.py my-api --description "My awesome API"
  python generate_project.py my-api --output ~/projects
        """
    )
    
    parser.add_argument(
        "project_name",
        help="專案名稱（例如：my-api）"
    )
    
    parser.add_argument(
        "--description",
        default="FastAPI Application",
        help="專案描述（預設：FastAPI Application）"
    )
    
    parser.add_argument(
        "--output",
        type=Path,
        default=Path.cwd(),
        help="輸出目錄（預設：當前目錄）"
    )
    
    parser.add_argument(
        "--no-git",
        action="store_true",
        help="不初始化 Git repository"
    )
    
    args = parser.parse_args()
    
    generate_project(
        project_name=args.project_name,
        description=args.description,
        output_dir=args.output,
        init_git=not args.no_git
    )


if __name__ == "__main__":
    main()
