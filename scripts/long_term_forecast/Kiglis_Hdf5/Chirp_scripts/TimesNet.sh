model_name=TimesNet

python -u run.py \
  --task_name long_term_forecast \
  --is_training 1 \
  --root_path ./dataset/Kiglis_hdf5_2.0/Chirp/ \
  --data_path training_data_chirp_10km.hdf5 \
  --model_id chirp_30_1 \
  --model $model_name \
  --data Kiglis_Hdf5 \
  --features MS \
  --seq_len 96 \
  --label_len 0 \
  --pred_len 1 \
  --e_layers 2 \
  --d_layers 1 \
  --factor 3 \
  --enc_in 30 \
  --dec_in 30 \
  --c_out 30 \
  --batch_size 10 \
  --d_model 512 \
  --des 'Exp' \
  --itr 1 \