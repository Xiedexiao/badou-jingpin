"""
配置
"""

Config = {
    "model_path": "output",
    "train_data_path": "E:\八斗人工智能-精品班\第七周 文本分类\week7 文本分类问题\文本分类练习.csv",
    "valid_data_path": "../data/valid_tag_news.json",
    "vocab_path": "./data/vocab.txt",
    "model_type":"lstm",
    "max_length": 20,
    "hidden_size": 128,
    "kernel_size": 3,
    "num_layers": 2,
    "epoch": 15,
    "batch_size": 64,
    "pooling_style":"max",
    "optimizer": "adam",
    "learning_rate": 1e-3,
    "pretrain_model_path":r"F:\Desktop\work_space\pretrain_models\bert-base-chinese",
    "seed": 987
}