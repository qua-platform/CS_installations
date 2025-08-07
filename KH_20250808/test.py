#!/usr/bin/env python3
"""
Script to update all experiment dashboard modules to use dynamic theme.
This will replace 'template="dashboard_dark"' with 'template=get_theme_template()'
in all experiment files.
"""

import os
import re
from pathlib import Path

def update_experiment_file(filepath):
    """Update a single experiment file to use dynamic theme"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already updated
    if 'get_theme_template' in content:
        print(f"✓ {filepath.name} already updated")
        return False
    
    # Add import for plotly.io if not present
    if 'import plotly.io as pio' not in content:
        # Find the last import line
        import_lines = re.findall(r'^import.*$|^from.*import.*$', content, re.MULTILINE)
        if import_lines:
            last_import = import_lines[-1]
            content = content.replace(
                last_import, 
                f"{last_import}\nimport plotly.io as pio"
            )
    
    # Add the get_theme_template function after imports
    insert_pos = content.find('\n\n', content.rfind('import'))
    if insert_pos != -1:
        theme_function = '''

# --------------------------------------------------------------------
# Helper to get current theme
# --------------------------------------------------------------------
def get_theme_template():
    """Get the current theme template for plotly figures."""
    current = pio.templates.default
    if current in ['dashboard_dark', 'dashboard_light']:
        return current
    return 'dashboard_dark'
'''
        content = content[:insert_pos] + theme_function + content[insert_pos:]
    
    # Replace all occurrences of template="dashboard_dark"
    content = re.sub(
        r'template\s*=\s*["\']dashboard_dark["\']',
        'template=get_theme_template()',
        content
    )
    
    # Save the updated file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated {filepath.name}")
    return True

def main():
    """Update all experiment dashboard files"""
    experiments_dir = Path('experiments')
    
    if not experiments_dir.exists():
        print("❌ 'experiments' directory not found!")
        return
    
    # Get all dashboard Python files
    dashboard_files = list(experiments_dir.glob('*_dashboard.py'))
    
    print(f"Found {len(dashboard_files)} experiment dashboard files\n")
    
    updated_count = 0
    for filepath in dashboard_files:
        if update_experiment_file(filepath):
            updated_count += 1
    
    print(f"\n🎉 Updated {updated_count} files!")
    print("\nDon't forget to:")
    print("1. Save the updated main_dashboard.py")
    print("2. Create theme_helper.py (if using modular approach)")
    print("3. Test the theme switching functionality")

if __name__ == "__main__":
    main()