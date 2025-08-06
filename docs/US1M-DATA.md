
# Preparing US-1M Dataset
This document provides detailed instructions on preparing UniMed dataset for pre-training contrastive medical VLMs. Note that, although UniMed is developed using fully open-source medical data sources, we are not able to release the processed data directly, as some data-sources are subject to strict distribution licenses. Therefore, we provide step-by-step instructions on assembling UniMed data and provide several parts of UniMed for which no licensing obligations are present.

Follow the instructions below to construct US-1M dataset.


## Downloading Individual Datasets and Converting them into Image-text format

As the first step, we download the individual Medical Datasets from their respective data providers.  We suggest putting all datasets under the same folder (say `$DATA`) to ease management. The file structure looks like below.
```
$DATA/
|-- 0001-Cls-FETAL_PLANES_ZENODO/
|-- 0002-Seg-CAMUS-Human_Heart_Project/
|-- 0003-CDS-BUSI-Kaggle/
|-- 0004-Seg-JNU_IFM-Kaggle/
|-- 0005-Seg-DDTI-Kaggle/
|-- 0006-Cls-UBIBC-Kaggle/
|-- 0007-Cls-PCOS-Kaggle/
|-- 0008-Analysis-CAUCD-Kaggle/
|-- 0009-Estimate-US_Seq-Kaggle/
|-- 0010-Registration-MRI_US_Brain-Kaggle/
|-- ...
```

Datasets list:
- [CheXpert](#1.-CheXpert)
- [MIMIC-CXR](#2.-mimic-cxr)
- [OpenI](#openi)
- [ChestX-ray8](#chestx-ray8)
- [RadImageNet](#radimagenet)
- [Retinal-Datasets](#retinal-datasets)
- [Quilt-1M](#quilt-1m)
- [PMC-OA](#pmc-oa)
- [ROCO-V2](#roco-v2)
- [LLaVA-Med](#LLaVA-Med)

We use the scripts provided in `data_prepration_scripts` for preparing UniMed dataset. Follow the instructions illustrated below.

### 1. CheXpert
#### Downloading Dataset: 
  - Step 1: Download the dataset from the following [link](https://www.kaggle.com/datasets/ashery/chexpert) on Kaggle.

#### Downloading Annotations:
  - Download the processed text annotations file `chexpert_with_captions_only_frontal_view.csv` from this [link](https://mbzuaiac-my.sharepoint.com/:f:/g/personal/uzair_khattak_mbzuai_ac_ae/Es0rzhS3MZNHg1UyB8AWPKgB5D0KcrRSOQOGYM7gDkOmRg?e=j6VHof), and put it to the main folder.
  - The final directory structure should look like below.

```
CheXpert-v1.0-small/
|–– train/
|–– valid/
|–– train.csv
|–– valid.csv
|–– chexpert_with_captions_only_frontal_view.csv
```

#### Preparing image-text dataset and conversion in webdataset format: 
  - Run the following command to create image-text dataset:
  - `python data_prepration_scripts/CheXpert/webdataset_chexpert.py --csv_file chexpert_with_captions_only_frontal_view.csv --output_dir <path-to-save-all-image-text-datasets>/chexpert_webdataset --parent_dataset_path $DATA/CheXpert-v1.0-small`
  - This will prepare chexpert image-text data in webdataset format, to be used directly for training.

### 2. MIMIC-CXR
#### Downloading Dataset:
  - Step 1: Follow the instructions in the following [link](https://physionet.org/content/mimic-cxr-jpg/2.1.0/) to get access to the Mimic CXR jpg dataset (Note you have to complete a data-usage agreement form inorder to get access to the dataset).
  - Step 2: Then, download the 10 folders p10-p19 from [link](https://physionet.org/content/mimic-cxr-jpg/2.1.0/files/).

#### Downloading Annotations:
  - Download the processed text annotations folder `mimic_cxr_with_captions_and_reports_only_frontal_view.csv` from this [link](https://mbzuaiac-my.sharepoint.com/:f:/g/personal/uzair_khattak_mbzuai_ac_ae/Es0rzhS3MZNHg1UyB8AWPKgB5D0KcrRSOQOGYM7gDkOmRg?e=j6VHof), and put it to the main folder.
  - The final directory structure should look like below.
```
mimic-cxr-jpg/2.0.0/files/
|-- mimic_cxr_with_captions_and_reports_only_frontal_view.csv
|–– p10/
|–– p11/
|–– p12/
...
...
|–– p19/
```

#### Preparing image-text datasets in webdataset format: 
  - Run the following command to create image-text dataset:
  - `python data_prepration_scripts/MIMIC-CXR/webdataset_mimic_cxr.py --csv_file mimic_cxr_with_captions_and_reports_only_frontal_view.csv --output_dir <path-to-save-all-image-text-datasets>/mimic_cxr_webdataset --parent_dataset_path $DATA/mimic-cxr-jpg`
  - This will prepare mimic-cxr image-text data in webdataset format, to be used directly for training.


### 3. OpenI
#### Downloading Dataset: 
  - Step 1 : Download the OpenI PNG dataset from the [link](https://openi.nlm.nih.gov/imgs/collections/NLMCXR_png.tgz).

#### Downloading Annotations:
  - Download the processed text annotations folder `openai_refined_concepts.json`, and `filter_cap.json` from this [link](https://mbzuaiac-my.sharepoint.com/:f:/g/personal/uzair_khattak_mbzuai_ac_ae/Es0rzhS3MZNHg1UyB8AWPKgB5D0KcrRSOQOGYM7gDkOmRg?e=j6VHof), and put it to the main folder.
  - The final directory structure should look like below.

```
openI/
|-- openai_refined_concepts.json
|-- filter_cap.json
|–– image/
    |-- # image files ...
```

#### Preparing image-text datasets in webdataset format: 
  - Run the following command to create image-text dataset:
  - `python data_prepration_scripts/Openi/openi_webdataset.py --original_json_file_summarizations_path filter_cap.json --gpt_text_descriptions_path openai_refined_concepts.json --output_dir <path-to-save-all-image-text-datasets>/openi_webdataset --parent_dataset_path $DATA/OpenI/image`
  - This will prepare openi image-text data in webdataset format, to be used directly for training.

### 4. ChestX-ray8
#### Downloading Dataset:
  - Step 1: Download the images folder from the following [link](https://nihcc.app.box.com/v/ChestXray-NIHCC).

#### Downloading Annotations:
  - Download the processed text annotations folder `Chest-Xray8_with_captions.csv` from this [link](https://mbzuaiac-my.sharepoint.com/:f:/g/personal/uzair_khattak_mbzuai_ac_ae/Es0rzhS3MZNHg1UyB8AWPKgB5D0KcrRSOQOGYM7gDkOmRg?e=j6VHof), and put it to the main folder.
  - The final directory structure should look like below.
```
chest_xray8/
|-- Chest-Xray8_with_captions.csv
|–– images/
    |-- # image files ...
```

#### Preparing image-text dataset and conversion in webdataset format: 
  - Run the following command to create image-text dataset:
  - `python data_prepration_scripts/ChestX-ray8/chest-xray_8_webdataset.py --csv_file Chest-Xray8_with_captions.csv --output_dir <path-to-save-all-image-text-datasets>/chest_xray8_webdataset --parent_dataset_path $DATA/chest_xray8/images`
  - This will prepare chest-xray8 image-text data in webdataset format, to be used directly for training.

### 5. RadImageNet
#### Downloading Dataset:
  - Step 1 : Submit the request for dataset via the [link](https://www.radimagenet.com/) and,
  - Step 2 : Download the official dataset splits csv from this [link](https://drive.google.com/drive/folders/1FUir_Y_kbQZWih1TMVf9Sz8Pdk9NF2Ym?usp=sharing). [Note that the access to the dataset-split will be granted once the request for dataset usage (in step 1) is approved]


#### Downloading Annotations:
  - Download the processed text annotations folder `radimagenet_with_captions_training_set.csv` from this [link](https://mbzuaiac-my.sharepoint.com/:f:/g/personal/uzair_khattak_mbzuai_ac_ae/Es0rzhS3MZNHg1UyB8AWPKgB5D0KcrRSOQOGYM7gDkOmRg?e=j6VHof), and put it to the main folder.
  - The final directory structure should look like below.

  - The directory structure should look like below.
```
radimagenet/
|–– radiology_ai/
    |-- radimagenet_with_captions_training_set.csv
    |-- CT
    |-- MR
    |-- US
```

#### Preparing image-text dataset and conversion in webdataset format: 
  - Run the following command to create image-text dataset:
  - `python data_prepration_scripts/RadImageNet/radimagenet_webdataset.py --csv_file radimagenet_with_captions_training_set.csv --output_dir <path-to-save-all-image-text-datasets>/radimagenet_webdataset --parent_dataset_path $DATA/radimagenet`
  - This will prepare chest-xray8 image-text data in webdataset format, to be used directly for training.

### 6. Retinal-Datasets

For the retinal datasets, we select 35 Retinal datasets and convert the label only datasets into multi-modal versions using LLM-in-the-loop pipeline proposed in the paper. 
#### Downloading Datasets: 
  - Part 1: Download the MM-Retinal dataset available from the official [google drive link](https://drive.google.com/drive/folders/177RCtDeA6n99gWqgBS_Sw3WT6qYbzVmy).

  - Part 2: Download the datasets presented in the table below to prepare the FLAIR Dataset collection (table source: [FLAIR](https://github.com/jusiro/FLAIR/)).


|                                                                                                                                      |                                                                                                      |                                                                             |     |                                                                                                                                                                 |     |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| [08_ODIR-5K](https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k)                                            | [15_APTOS](https://www.kaggle.com/competitions/aptos2019-blindness-detection/data)                   | [35_ScarDat](https://github.com/li-xirong/fundus10k)                        |     | [29_AIROGS](https://zenodo.org/record/5793241#.ZDi2vNLMJH5)                                                                                                     |
| [09_PAPILA](https://figshare.com/articles/dataset/PAPILA/14798004/1)                                                                 | [16_FUND-OCT](https://data.mendeley.com/datasets/trghs22fpg/3)                                       | [23_HRF](http://www5.cs.fau.de/research/data/fundus-images/)                |     | [30_SUSTech-SYSU](https://figshare.com/articles/dataset/The_SUSTech-SYSU_dataset_for_automated_exudate_detection_and_diabetic_retinopathy_grading/12570770/1)   |     |
| [03_IDRID](https://idrid.grand-challenge.org/Rules/)                                                                                 | [17_DiaRetDB1](https://www.it.lut.fi/project/imageret/diaretdb1_v2_1/)                               | [24_ORIGA](https://pubmed.ncbi.nlm.nih.gov/21095735/)                       |     | [31_JICHI](https://figshare.com/articles/figure/Davis_Grading_of_One_and_Concatenated_Figures/4879853/1)                                                        |     |
| [04_RFMid](https://ieee-dataport.org/documents/retinal-fundus-multi-disease-image-dataset-rfmid-20)                                  | [18_DRIONS-DB](http://www.ia.uned.es/~ejcarmona/DRIONS-DB.html)                                      | [26_ROC](http://webeye.ophth.uiowa.edu/ROC/)                                |     | [32_CHAKSU](https://figshare.com/articles/dataset/Ch_k_u_A_glaucoma_specific_fundus_image_database/20123135?file=38944805)                                      |     |
| [10_PARAGUAY](https://zenodo.org/record/4647952#.ZBT5xXbMJD9)                                                                        | [12_ARIA](https://www.damianjjfarnell.com/?page_id=276)                                              | [27_BRSET](https://physionet.org/content/brazilian-ophthalmological/1.0.0/) |     | [33_DR1-2](https://figshare.com/articles/dataset/Advancing_Bag_of_Visual_Words_Representations_for_Lesion_Classification_in_Retinal_Images/953671?file=6502302) |     |
| [06_DEN](https://github.com/Jhhuangkay/DeepOpht-Medical-Report-Generation-for-Retinal-Images-via-Deep-Models-and-Visual-Explanation) | [19_Drishti-GS1](http://cvit.iiit.ac.in/projects/mip/drishti-gs/mip-dataset2/Home.php)               | [20_E-ophta](https://www.adcis.net/en/third-party/e-ophtha/)                |     | [34_Cataract](https://www.kaggle.com/datasets/jr2ngb/cataractdataset)                                                                                           |     |
| [11_STARE](https://cecas.clemson.edu/~ahoover/stare/)                                                                                | [14_AGAR300](https://ieee-dataport.org/open-access/diabetic-retinopathy-fundus-image-datasetagar300) | [21_G1020](https://arxiv.org/abs/2006.09158)                                |     |                                                                                                                                                                 |     |


#### Downloading Annotations:
  - Download the processed text annotations folder `Retina-Annotations` from this [link](https://mbzuaiac-my.sharepoint.com/:f:/g/personal/uzair_khattak_mbzuai_ac_ae/Es0rzhS3MZNHg1UyB8AWPKgB5D0KcrRSOQOGYM7gDkOmRg?e=j6VHof).
  - The directory structure should look like below.
```
Retina-Datasets/
|-- Retina-Annotations/
|-- 03_IDRiD/
|-- 11_STARE/
...
```


#### Preparing image-text dataset and conversion in webdataset format: 
  - Run the following commands to create image-text datasets for Retinal datasets
```
   python data_prepration_scripts/Retinal-Datasets/retina_webdataset_part1.py --csv_files_directory <path-to-csv-files-directory> --output_dir <path-to-save-all-image-text-datasets>/retina_part1_webdataset/ --parent_dataset_path $DATA/Retina-Datasets
   python data_prepration_scripts/Retinal-Datasets/retina_webdataset_part2.py --csv_files_directory <path-to-csv-files-directory> --output_dir <path-to-save-all-image-text-datasets>/retina_part2_webdataset/ --parent_dataset_path $DATA/Retina-Datasets
   python data_prepration_scripts/Retinal-Datasets/retina_webdataset_part3.py --csv_files_directory <path-to-csv-files-directory> --output_dir <path-to-save-all-image-text-datasets>/retina_part3_webdataset/ --parent_dataset_path $DATA/Retina-Datasets 
  ```

  - This will prepare image-text data for retina-modality in webdataset format, to be used directly for training.


### Quilt-1M

Note: Quilt-1M provides image-text pairs, and we directly utilize their image-text pairs in our pretraining.

#### Downloading Dataset: 
  - Step 1:Request access for Quilt-1M dataset via the [link](https://zenodo.org/records/8239942), and then download the respective dataset.
  - The directory structure should look like below.
```
Quilt/
|-- quilt_1M_lookup.csv
|-- # bunch of files
|–– quilt_1m/
    |-- #images
```

#### Preparing image-text datasets in webdataset format: 
  - Run the following command:
  - `python data_prepration_scripts/Quilt-1M/quilt_1m_webdataset.py --csv_file $DATA/Quilt/quilt_1M_lookup.csv --output_dir <path-to-save-all-image-text-datasets>/quilt_1m_webdataset --parent_dataset_path $DATA/Quilt/quilt_1m/`
  - This will prepare Quilt-1M image-text data in webdataset format, to be used directly for training.

### PMC-OA

Note: PMC-OA provides image-text pairs, and we directly utilize their image-text pairs in our UniMed pretraining dataset.

#### Downloading Dataset:
  - Step 1: Download the PMC-OA images from the following [link](https://huggingface.co/datasets/axiong/pmc_oa/blob/main/images.zip).
  - Step 2: Download the json file ([link](https://huggingface.co/datasets/axiong/pmc_oa/resolve/main/pmc_oa.jsonl)).
  - The directory structure should look like below.
```
pmc_oa/
|–– pmc_oa.jsonl
|-- caption_T060_filtered_top4_sep_v0_subfigures
    |-- # iamges
|-- # bunch of files
```

#### Preparing image-text datasets in webdataset format: 
  - Run the following command:
  - `python data_prepration_scripts/PMC-OA/pmc_oa_webdataset.py --csv_file $DATA/pmc_oa/pmc_oa.jsonl --output_dir <path-to-save-all-image-text-datasets>/pmc_oa_webdataset/ --parent_dataset_path $DATA/pmc_oa/caption_T060_filtered_top4_sep_v0_subfigures/`
  - This will prepare PMC-OA image-text data in webdataset format, to be used directly for training.

### ROCO-V2
Note: ROCO-V2 provides image-text pairs, and we directly utilize their image-text pairs in our pretraining.

#### Downloading Dataset: 
  - Step 1: Download the images and captions from the [link](https://zenodo.org/records/8333645).
  - The directory structure should look like below.
```
ROCOV2/
|–– train/
|-- test/
|-- train_captions.csv
|-- # bunch of files
```

#### Preparing image-text datasets in webdataset format: 
  - Run the following command:
  - `python data_prepration_scripts/ROCOV2/roco_webdataset.py --csv_file $DATA/ROCOV2/train_captions.csv --output_dir <path-to-save-all-image-text-datasets>/rocov2_webdataset/ --parent_dataset_path $DATA/ROCOV2/train/`
  - This will prepare ROCOV2 image-text data in webdataset format, to be used directly for training.

### LLaVA-Med
Note: LLaVA-Med provides image-text pairs, and we directly utilize their image-text pairs in our pretraining.

#### Downloading Dataset:
  - Download images by following instructions at LLaVA-Med official repository [here](https://github.com/microsoft/LLaVA-Med?tab=readme-ov-file#data-download).

#### Downloading Annotations:
  - Download the filtered caption files `llava_med_instruct_fig_captions.json`, and `llava_med_alignment_500k_filtered.json` from this [link](https://mbzuaiac-my.sharepoint.com/:f:/g/personal/uzair_khattak_mbzuai_ac_ae/Es0rzhS3MZNHg1UyB8AWPKgB5D0KcrRSOQOGYM7gDkOmRg?e=j6VHof). The final directory should look like this:

```
llava_med/
|–– llava_med_alignment_500k_filtered.json
|-- llava_med_instruct_fig_captions.json
|-- images
    |-- # images
```

#### Preparing image-text datasets in webdataset format: 
  - Run the following commands:
```  
python data_prepration_scripts/LLaVA-Med/llava_med_alignment_webdataset.py --csv_file $DATA/llava_med/llava_med_alignment_500k_filtered.json --output_dir <path-to-save-all-image-text-datasets>/llava_med_alignment_webdataset/ --parent_dataset_path $DATA/llava_med/images/`
python data_prepration_scripts/LLaVA-Med/llava_med_instruct_webdataset.py --csv_file $DATA/llava_med/llava_med_instruct_fig_captions.json --output_dir <path-to-save-all-image-text-datasets>/llava_med_instruct_webdataset/ --parent_dataset_path $DATA/llava_med/images/`
```
  - This will prepare LLaVa-Med image-text data in webdataset format, to be used directly for training.


## Final Dataset Directory Structure:

After following the above steps, UniMed dataset will be now completely prepared in the webdataset format. The final directory structure looks like below:

``` 
<path-to-save-all-image-text-datasets>/
|–– chexpert_webdataset/
|–– mimic_cxr_webdataset/
|–– openi_webdataset/
|-- chest_xray8_webdataset/
|-- radimagenet_webdataset/
|-- retina_part1_webdataset/
|-- retina_part2_webdataset/
|-- retina_part3_webdataset/
|-- quilt_1m_webdataset
|–– pmc_oa_webdataset/
|-- rocov2_webdataset/
|–– llava_med_alignment_webdataset/
|–– llava_med_instruct_webdataset/
```
