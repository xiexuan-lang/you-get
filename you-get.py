import os
import sys

def add_src_to_path():
    """Add the src directory to the system path."""
    # 获取当前脚本的目录并构建源代码路径
    script_dir = os.path.dirname(os.path.realpath(__file__))
    src_dir = os.path.join(script_dir, 'src')
    sys.path.insert(1, src_dir)

def main():
    """Main function to execute the you-get script."""
    add_src_to_path()
    
    # 检查Python版本并导入you-get模块
    if sys.version_info[0] == 3:
        import you_get
        you_get.main(repo_path=os.path.dirname(sys.argv[0]))
    else:  # 处理Python 2
        from you_get.util import log
        log.e("[fatal] Python 3 is required!")
        log.wtf("Please run this script using 'python3 you-get'.")

if __name__ == '__main__':
    main()
