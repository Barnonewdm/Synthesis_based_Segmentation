#Env
export nnUNet_raw_data_base='/mnt/data1/weidongming/nnUNet/data/infant_raw/'
export nnUNet_preprocessed='/mnt/data1/weidongming/nnUNet/data/nnUNet_preprocessed/'
export RESULTS_FOLDER='/mnt/data1/weidongming/nnUNet/trained_models/'

#Preprocess
nnUNet_convert_decathlon_task -i ./data/infant_raw/Task01_Brain/
nnUNet_plan_and_preprocess -t 001 --verify_dataset_integrity

#Train
nnUNet_train 2d nnUNetTrainerV2 1 0 --deterministic
nnUNet_train 3d_fullres nnUNetTrainerV2 1 0 --deterministic

#Test
nnUNet_predict -i ./data/infant_raw/nnUNet_raw_data/Task007_Brain/imagesTs/ -o ./results/. -m 3d_fullres -t 007
