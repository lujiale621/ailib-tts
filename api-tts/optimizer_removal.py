from torch import load, save

if __name__ == '__main__':
    print("优化器通常不会被用于推理阶段，如果只用于推理可以去除优化器以减小模型体积\n")
    input_path = input("请输入模型的路径：")
    output_path = f"{input_path.split('.')[0]}_inference.pth"
    checkpoint_dict = load(input_path, map_location='cpu')
    checkpoint_dict_new = {}
    for k, v in checkpoint_dict.items():
        if k == "optimizer":
            print(f"remove optimizer")
            continue
        checkpoint_dict_new[k] = v
    save(checkpoint_dict_new, output_path)
    print("finish")
    print(output_path)
