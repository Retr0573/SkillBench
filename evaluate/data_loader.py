import json
import os
import glob


def read_skill(skill_dir):
    '''
    Read the skill data from the skill_dir
    - Args:
        skill_dir: the directory of the skill data

    - Returns:
        results: a dictionary of the skill data
        results = {
            '1': { # level
                {
                    "0": { # prompt_id
                        "objects": ["apple", "banana"],
                        "tags": ["..."],
                        "prompt": "A red apple and a yellow banana."
                    },    
                    "1": {
                        "objects": ["apple", "banana"],
                        "tags": ["..."],
                        "prompt": "A yellow apple and a green banana."
                    }
                    ...
                }
            },
            ...
        }
    '''
    results = {}
    txt_file_paths = glob.glob(os.path.join(skill_dir, '*.json'))
    for txt_file_path in sorted(txt_file_paths):
        # 检查文件名里有没有包含数字，将该数字记录成一个变量：level
        level = ''.join(
            filter(str.isdigit, os.path.basename(txt_file_path)))  # like: "3"
        # results.setdefault(level, )
        with open(txt_file_path, 'r') as f:
            data = json.load(f)
        results[level] = data
    return results


if __name__ == "__main__":
    skill_dir = 'data/cross_counting_attribute_binding_spatial'
    skill_data = read_skill(skill_dir)
    for level, datas in skill_data.items():
        print(f"Level: {level}")
        print(datas)
        for p_id in datas:
            data = datas[p_id]
            objects = data['objects']
            tags = data['tags']
            prompt_text = data['prompt']
            print(f"Prompt_id: {p_id}", f"Objects: {objects}", f"Tags: {tags}",
                  f"Prompt: {prompt_text}")
