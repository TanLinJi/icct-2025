import pickle
import json
import numpy as np
from pathlib import Path

def convert_numpy(obj):
    """递归转换NumPy类型为Python基本类型"""
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: convert_numpy(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy(x) for x in obj]
    else:
        return obj

def json_dumps_custom(obj, indent=4, current_indent=0):
    """
    自定义JSON序列化：
    - 字典层级正常缩进（indent控制）
    - 纯基本类型的列表（int/float/str等）紧凑显示为一行
    - 嵌套列表/字典保持结构缩进
    """
    if isinstance(obj, dict):
        indent_str = ' ' * current_indent
        items = []
        for key, value in obj.items():
            key_str = json.dumps(key)  # 处理键的引号
            value_str = json_dumps_custom(value, indent=indent, current_indent=current_indent + indent)
            items.append(f"{indent_str}{key_str}: {value_str}")
        return '{\n' + ',\n'.join(items) + f'\n{indent_str}}}'
    
    elif isinstance(obj, list):
        # 检查是否所有元素都是基本类型（int/float/str/bool/None）
        basic_types = (int, float, str, bool, type(None))
        if all(isinstance(x, basic_types) for x in obj):
            # 紧凑显示：元素用逗号连接
            elements = [json.dumps(x) for x in obj]
            return '[' + ', '.join(elements) + ']'
        else:
            # 嵌套结构：正常缩进，元素缩进 current_indent + indent
            elem_indent = current_indent + indent
            elem_indent_str = ' ' * elem_indent
            elements = []
            for x in obj:
                elem_str = json_dumps_custom(x, indent=indent, current_indent=elem_indent)
                elements.append(f"{elem_indent_str}{elem_str}")
            return '[\n' + ',\n'.join(elements) + f'\n{" " * current_indent}]'
    
    else:
        # 基本类型直接转换
        return json.dumps(obj)

def pkl_to_txt(input_path: str, output_path: str = None, indent: int = 4) -> None:
    """
    将pkl文件转换为可读txt（优化列表显示）
    :param input_path: pkl文件路径
    :param output_path: 输出txt路径（默认同目录同名txt）
    :param indent: 字典层级缩进空格数（默认4）
    """
    if output_path is None:
        output_path = Path(input_path).with_suffix('.txt')
    
    try:
        # 读取并转换NumPy类型
        with open(input_path, 'rb') as f:
            data = pickle.load(f)
        data = convert_numpy(data)
        
        # 自定义序列化
        formatted_json = json_dumps_custom(data, indent=indent)
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(formatted_json)
        
        print(f"✅ 转换成功！保存至：{output_path}")
    
    except FileNotFoundError:
        print(f"❌ 错误：文件不存在 - {input_path}")
    except pickle.UnpicklingError:
        print(f"❌ 错误：无效的pkl文件 - {input_path}")
    except Exception as e:
        print(f"❌ 未知错误：{e}")

if __name__ == "__main__":
    # 替换为你的pkl文件路径
    input_path = '/home/jtl/embodied_models/src/data/tools/sam2/gui/testData/0000000000_result.pkl'
    pkl_to_txt(input_path)