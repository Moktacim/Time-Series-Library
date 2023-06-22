export CUDA_VISIBLE_DEVICES=1

model_name=Autoformer
# debuging 
python -u run.py \
  --task_name long_term_forecast \
  --is_training 1 \
  --root_path ./dataset/Kiglis_hdf5/CD \
  --data_path training_data_5km.hdf5 \
  --model_id cdonly_30_1 \
  --model $model_name \
  --data Kiglis_Hdf5 \
  --features MS \
  --seq_len 96 \
  --label_len 48 \
  --pred_len 96 \
  --e_layers 2 \
  --d_layers 1 \
  --factor 3 \
  --enc_in 321 \
  --dec_in 321 \
  --c_out 321 \
  --des 'Exp' \
  --itr 1