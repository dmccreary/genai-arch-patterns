#!/usr/bin/env python3
"""
Image Compression Script for GenAI Architecture Patterns Website
Compresses large images to approximately 300KB in PNG format for web optimization
"""

import os
import sys
from PIL import Image, ImageOps
import shutil
from pathlib import Path

def get_file_size_kb(filepath):
    """Get file size in KB"""
    return os.path.getsize(filepath) / 1024

def compress_image(input_path, target_size_kb=300, min_compression=0, max_compression=9):
    """
    Compress an image to approximately the target size in KB using PNG format

    Args:
        input_path: Path to input image
        target_size_kb: Target size in KB (default 300)
        min_compression: Minimum PNG compression level (0=fastest)
        max_compression: Maximum PNG compression level (9=best compression)
    """
    try:
        # Create backup
        backup_path = str(input_path) + ".backup"
        if not os.path.exists(backup_path):
            shutil.copy2(input_path, backup_path)
            print(f"  Backup created: {backup_path}")
        
        # Open and optimize image
        with Image.open(input_path) as img:
            # Preserve transparency for PNG format
            if img.mode in ('RGBA', 'LA'):
                # Keep RGBA mode for PNG with transparency
                pass
            elif img.mode == 'P':
                # Convert palette mode to RGBA to preserve any transparency
                img = img.convert('RGBA')
            elif img.mode not in ('RGB', 'RGBA'):
                # Convert other modes to RGB
                img = img.convert('RGB')
            
            # Apply auto-orientation based on EXIF data
            img = ImageOps.exif_transpose(img)
            
            original_size = get_file_size_kb(input_path)
            
            # If already small enough, skip
            if original_size <= target_size_kb:
                print(f"  Already optimized: {original_size:.1f}KB")
                return True

            # Get original dimensions
            original_width, original_height = img.size
            print(f"  Original dimensions: {original_width}x{original_height}")

            # Try compression first with maximum setting
            best_compression = 9
            best_size = float('inf')
            best_img = img.copy()

            # Try different resize factors - be more aggressive for very large files
            if original_size > 1000:  # Over 1MB, start with smaller sizes
                resize_factors = [0.6, 0.5, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15]
            elif original_size > 500:  # Over 500KB
                resize_factors = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.25, 0.2]
            else:  # Smaller files, try compression first
                resize_factors = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.25, 0.2]

            for resize_factor in resize_factors:
                # Resize image if needed
                if resize_factor < 1.0:
                    new_width = int(original_width * resize_factor)
                    new_height = int(original_height * resize_factor)
                    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    print(f"  Trying resize: {resize_factor:.1%} ({new_width}x{new_height})")
                else:
                    resized_img = img
                    print(f"  Trying original size with max compression")

                # Try with maximum PNG compression
                temp_path = str(input_path) + ".temp"
                resized_img.save(temp_path, "PNG", compress_level=9, optimize=True)
                temp_size = get_file_size_kb(temp_path)

                print(f"    Result: {temp_size:.1f}KB")

                # If we found a size that works, save it
                if temp_size <= target_size_kb:
                    best_size = temp_size
                    best_img = resized_img.copy()
                    final_width, final_height = resized_img.size
                    print(f"  ✓ Found suitable size: {temp_size:.1f}KB at {final_width}x{final_height}")
                    os.remove(temp_path)
                    break

                os.remove(temp_path)

            # If we couldn't get under target size, use the smallest we achieved
            if best_size == float('inf'):
                print(f"  Warning: Could not reach target size, using smallest achieved")
                best_img = img.resize((int(original_width * 0.2), int(original_height * 0.2)), Image.Resampling.LANCZOS)
            
            # Save with best image found
            # Convert .jpg/.jpeg to .png format
            output_path = input_path
            if input_path.suffix.lower() in ['.jpg', '.jpeg']:
                output_path = input_path.with_suffix('.png')

            best_img.save(output_path, "PNG", compress_level=9, optimize=True)

            final_size = get_file_size_kb(output_path)
            compression_ratio = (1 - final_size / original_size) * 100
            final_width, final_height = best_img.size

            print(f"  Final result: {original_size:.1f}KB → {final_size:.1f}KB ({compression_ratio:.1f}% reduction)")
            print(f"  Dimensions: {original_width}x{original_height} → {final_width}x{final_height}")

            # If we converted JPG to PNG, remove the original JPG
            if output_path != input_path:
                os.remove(input_path)
                print(f"  Converted JPG to PNG: {input_path} → {output_path}")
            
            return True
            
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def find_large_images(root_dir, min_size_kb=500):
    """Find all images larger than min_size_kb"""
    large_images = []
    image_extensions = {'.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'}
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if any(file.endswith(ext) for ext in image_extensions):
                filepath = Path(root) / file
                size_kb = get_file_size_kb(filepath)
                if size_kb >= min_size_kb:
                    large_images.append((filepath, size_kb))
    
    return sorted(large_images, key=lambda x: x[1], reverse=True)

def main():
    # Find all large images
    print("🔍 Scanning for large images...")
    # Navigate to repo root from src/resize-images/
    repo_root = Path(__file__).parent.parent.parent
    docs_dir = repo_root / "docs"
    large_images = find_large_images(docs_dir, min_size_kb=500)
    
    if not large_images:
        print("✅ No large images found (>500KB)")
        return
    
    print(f"\n📊 Found {len(large_images)} images larger than 500KB:")
    total_original_size = 0
    
    for filepath, size_kb in large_images:
        print(f"  {filepath}: {size_kb:.1f}KB")
        total_original_size += size_kb
    
    print(f"\n📈 Total size of large images: {total_original_size:.1f}KB ({total_original_size/1024:.1f}MB)")
    
    # Automatically proceed with compression
    print(f"\n🚀 Starting compression of {len(large_images)} images to ~300KB each...")
    
    # Compress images
    print(f"\n🔄 Compressing {len(large_images)} images...")
    successful = 0
    failed = 0
    total_final_size = 0
    
    for i, (filepath, original_size) in enumerate(large_images, 1):
        print(f"\n[{i}/{len(large_images)}] Processing: {filepath}")
        
        if compress_image(filepath, target_size_kb=300):
            successful += 1
            # Get new size (handle JPG->PNG conversion)
            if filepath.suffix.lower() in ['.jpg', '.jpeg']:
                new_path = filepath.with_suffix('.png')
                if new_path.exists():
                    total_final_size += get_file_size_kb(new_path)
                else:
                    total_final_size += get_file_size_kb(filepath)
            else:
                total_final_size += get_file_size_kb(filepath)
        else:
            failed += 1
            total_final_size += original_size  # Keep original size if failed
    
    # Summary
    print(f"\n✅ Compression Complete!")
    print(f"📊 Results:")
    print(f"  • Successful: {successful}")
    print(f"  • Failed: {failed}")
    print(f"  • Original total: {total_original_size:.1f}KB ({total_original_size/1024:.1f}MB)")
    print(f"  • Final total: {total_final_size:.1f}KB ({total_final_size/1024:.1f}MB)")
    
    if total_original_size > 0:
        savings = total_original_size - total_final_size
        savings_percent = (savings / total_original_size) * 100
        print(f"  • Saved: {savings:.1f}KB ({savings/1024:.1f}MB, {savings_percent:.1f}%)")
    
    print(f"\n💡 Backup files (.backup) created for safety")
    print(f"🔗 Update any markdown files that reference converted JPG→PNG files")

if __name__ == "__main__":
    main()