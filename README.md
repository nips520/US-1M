# US-1M: A Unified and Hierarchical Dataset for Pretraining Ultrasound Imaging Models

<p align="center">
    <img src="https://i.imgur.com/waxVImv.png" alt="Image">
</p>


This repository contains the code implementation for US-1M, which establishes a new benchmark in medical imaging research, comprising 1.28 million rigorously annotated ultrasound images with precise anatomical structure delineations and comprehensive demographic metadata.

---


# Updates
* **May 23, 2025**
  * Demo released on Hugging Face spaces ([view demo](https://huggingface.co/datasets/wyh1128/US-1M)).
* **Apr 13, 2025**
  * Annotations and code scripts for preparing the US-1M pretraining dataset are released.
  * US-1M training and inference code are released, along with pretrained checkpoints.
---

# Highlights

![main figure](docs/fig_dataset_statistics.png)


> **<p align="justify"> Abstract:** *Foundation models have made impressive strides in medical AI research, providing valuable features for downstream tasks and enabling task-specific models to adapt to new settings with minimal or no additional examples.
However, their application in  ultrasound (US) domain remains limited due to the lack of large-scale and openly accessible US medical datasets.
To fill this gap, we introduce US-1M, a comprehensive and unified ultrasound dataset featuring multi-organ, multi-center, multi-device, and multi-race coverage, comprising over 1 million images. Building on US-1M, we demonstrate its versatility through three representative tasks across three critical medical applications: organ segmentation, disease classification, and image enhancement. Our experiments reveal substantial performance gains in multiple ultrasound imaging tasks, establishing new benchmarks for ultrasound-based AI models. The unified and hierarchical architecture of US-1M opens new research frontiers in medical imaging, particularly for ultrasound analysis. * </p>

### US-1M: A Unified and Hierarchical Dataset for Pretraining Ultrasound Imaging Models

Main contributions of our work are:
1) We present **US-1M**, the first large-scale, openly accessible, and hierarchical ultrasound imaging dataset comprising 1.28 million clinically validated images collected worldwide. This dataset serves as a cornerstone for foundation model research in medical US imaging.
2) We demonstrate **US-1M** clinical versatility through foundation model pretraining, with experimental results confirming its utility in developing robust, generalizable models across diverse medical US tasks.
3) By conducting case study on accuracy analysis we shed new insights into US foundation model architetures.

Table 1: Quantitative comparison results on organ segmentation (mean ± std).
| Method      | Paper    | Pretrained on ImageNet |  | Pretrained on US-1M    |  |
|-------------|----------|:----------------------:|:---------------------:|:----------------------:|:------------------:|
|             |          | DSC (%) ↑  |  NSD (%) ↑ | DSC (%) ↑  |  NSD (%) ↑ |
| U-Net       | [Link](https://arxiv.org/abs/1505.04597) |   72.69 ± 1.89   |  76.10 ± 1.79   |   **75.23 ± 1.47** | **78.40 ± 1.26**  |
| DeepLabv3   | [Link](https://arxiv.org/abs/1706.05587) |   76.65 ± 1.64   |  80.29 ± 1.68   |   **78.72 ± 1.56** | **82.77 ± 1.07**  |
| SwinUNETR   | [Link](https://arxiv.org/abs/2201.01266) |   78.62 ± 1.92   |  82.62 ± 1.39   |   **80.49 ± 1.67** | **83.57 ± 1.39** | 

Table 2: Quantitative comparison results on disease classification (mean ± std).
| Method      | Paper    | Pretrained on ImageNet |  |  | Pretrained on US-1M    | |   |
|-------------|----------|:-----------:|:--------:|:----------:|:---------:|:-----------:|:---------:|
|             |          | Macro-F1 (%) ↑| Precision (%) ↑ |Recall (%) ↑ |Macro-F1 (%) ↑| Precision (%) ↑ |Recall (%) ↑|
| ResNet50 | [Link](https://arxiv.org/abs/1512.03385) |  58.21 ± 2.23 |59.10 ± 3.99 |58.53 ± 2.18 |**59.21 ± 2.16** |**60.69 ± 3.44** |**59.62 ± 2.18** |
|Swin-Transformer v2| [Link](https://arxiv.org/abs/2111.09883) |  60.15 ± 1.56 |59.30 ± 1.97 |60.78 ± 1.76 |**62.53 ± 1.35** |**65.27 ± 2.88** |**61.58 ± 1.50**|

Table 3: Quantitative comparison results on image enhancement (mean ± std).
| Method      | Paper    | Pretrained on ImageNet |  | | | Pretrained on US-1M    | |  | |
|-------------|----------|:-----------:|:--------:|:-----:|:------:|:---------:|:-----------:|:-----:|:-----:|
|             |          | NIQE (%) ↓| BRISQUE (%) ↓ |PIQE (%) ↑ |FID (%) ↓| NIQE (%) ↓ |BRISQUE (%) ↓| PIQE (%) ↑ |FID (%) ↓|
| CycleGAN | [Link](https://arxiv.org/abs/1703.10593) |7.12 ± 2.04 |31.68 ± 3.92 |29.24 ± 3.31 |118.6 ± 9.18| **6.85 ± 1.59**| **20.74 ± 2.97** |**30.26 ± 3.61**| **62.53 ± 6.78**|
|CUT | [Link](https://arxiv.org/abs/2007.15651) | 7.16 ± 1.86| 37.91 ± 4.34| 43.26 ± 3.78 |143.5 ± 9.59| **6.77 ± 1.42**| **21.8 ± 2.46** |**30.26 ± 2.84** |**61.81 ± 6.11**|
|EnlightenGAN  | [Link](https://doi.org/10.1109/TIP.2021.3051462) |6.76 ± 1.86 |22.83 ± 2.43 |**28.6 ± 2.36** |60.24 ± 3.08 |**6.55 ± 1.20** |**17.68 ± 2.50** |**30.18 ± 2.84**| **58.71 ± 4.25**|
## Installation

Before using US-1M for training and inference, please refer to the installation instructions described at [INSTALL.md](docs/INSTALL.md)


## Pre-trained Models

We provide 2 model weights for US-1M as listed in the table below. 

| `model_name`       |                                                                               `pretrained_weights`                                                                               | Res. |      GPUs       | Avg. score on 21 datasets |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----:|:---------------:|:-------------------------:|
| ResNet50 |          [`resnet50`](https://drive.google.com/file/d/1-A6a4JuLpqdA14CSmcb4xslRBYU3zstn/view?usp=sharing)           | 256  | 8 x A100 (40G) |           61.63           |
| SwinTransformer-B-16 | [`swintransformer`](https://drive.google.com/file/d/1lM_FbPsIjhVLdcYqwKBIp9mmwbHIFzeG/view?usp=sharing) | 256  | 8 x A100 (40G) |           62.09           |


## Preparing Dataset

For preparing US-1M pretraining dataset, we provide instructions for i) Downloading raw datasets from publicly available sources and ii) downloading processed annotations and merging with raw-datasets to build US-1M 
Refer to the detailed instructions described in [US1M-DATA.md](docs/US1M-DATA.md).
