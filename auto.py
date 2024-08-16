#!/usr/bin/env python3
# coding=utf-8
import os
import glob
import argparse

def generate_implementation(header_file, output_dir, include_dir):
    # 构建实现文件的路径
    impl_file = os.path.join(output_dir, os.path.basename(header_file).replace('.h', '.cpp'))

    # 检查实现文件是否已经存在
    if os.path.exists(impl_file):
        print(f"Skipped: {impl_file} already exists.")
        return
    
    with open(header_file, 'r') as f:
        lines = f.readlines()

    with open(impl_file, 'w') as f:
        # 生成包含头文件的 include 语句
        include_path = os.path.join(include_dir, os.path.basename(header_file))
        f.write('#include "{}"\n\n'.format(include_path))

        class_name = None
        for line in lines:
            stripped_line = line.strip()

            # 检查是否为类声明
            if stripped_line.startswith('class '):
                class_name = stripped_line.split()[1].split('{')[0].strip()

            # 检查是否为函数声明
            if stripped_line.endswith(';') and '(' in stripped_line and ')' in stripped_line:
                # 处理修饰符 (如 explicit, virtual)
                parts = stripped_line.split()
                modifiers = []
                return_type = ""
                func_name = ""
                params = ""

                # 提取修饰符、返回类型、函数名和参数列表
                for part in parts:
                    if part in ('explicit', 'virtual', 'inline', 'static', 'constexpr'):
                        modifiers.append(part)
                    elif '(' in part:  # 检测到函数名开始
                        func_name = part.split('(')[0]
                        params = stripped_line.split(func_name)[1]
                        break
                    else:
                        return_type += part + " "

                return_type = return_type.strip()
                modifiers_str = " ".join(modifiers)

                # 构建函数实现字符串
                func_impl = f'{modifiers_str} {return_type} {class_name}::{func_name}{params}'
                func_impl = func_impl.replace(';', ' {\n\n}\n')

                f.write(func_impl + '\n')

    print(f"Generated implementation file: {impl_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate .cpp implementation files from .h header files.")
    parser.add_argument('-d', '--directory', action='store_true', help="Place implementation files in ../src directory.")
    
    args = parser.parse_args()

    if args.directory:
        output_dir = os.path.join('..', 'src')
        include_dir = '../include'
        os.makedirs(output_dir, exist_ok=True)
    else:
        output_dir = '.'
        include_dir = '.'

    # 使用 glob 模块查找当前目录下所有 .h 文件
    header_files = glob.glob('*.h')
    
    if not header_files:
        print("No header files found in the current directory.")
    else:
        for header_file in header_files:
            generate_implementation(header_file, output_dir, include_dir)

